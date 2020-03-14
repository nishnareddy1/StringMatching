import time

file1 = open(r"../A_tale_of_two_cities.txt", "r", encoding="utf8")
file2 = open(r"../Longest_Pattern", "r", encoding="utf8")
#Pattern="ribonucleoside-diphosphate reductase1"
pattern=file2.read()
text = file1.read()

d = 256  # d is the number of characters in the input alphabet
q = 101  # A prime number


def search(pattern, text, q):
    if pattern == "":
        print("Pattern is empty")
        return -1

    patLen = len(pattern)
    textLen = len(text)
    patternMatch = 0
    j = 0
    p = 0  # hash value for Longest_Pattern
    t = 0  # hash value for text
    h = 1

    # The value of h would be "pow(d, M-1)% q"
    for i in range(patLen - 1):
        h = (h * d) % q

        # Calculate the hash value of Longest_Pattern and first window of text
    for i in range(patLen):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

        # Slide the Longest_Pattern over text one by one
    for i in range(textLen - patLen + 1):
        # Check the hash values of current window of text and
        # Longest_Pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(patLen):
                if text[i + j] != pattern[j]:
                    break

            j += 1
            # if p == t and Longest_Pattern[0...M-1] = text[i, i + 1, ...i + M-1]
            if j == patLen:
                patternMatch += 1
                print("Pattern found at index ", str(i))

                # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < textLen - patLen:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + patLen])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q
    if patternMatch == 0:
        print("Pattern not found in given text.")
            # Driver program to test the above function


start_time = time.time()
search(pattern, text, q)
finish_time = time.time()
print("execution time %s" % (finish_time - start_time))
