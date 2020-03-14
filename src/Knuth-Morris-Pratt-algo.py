import time

file1 = open(r"../A_tale_of_two_cities.txt", "r", encoding="utf8")
file2 = open(r"../Longest_Pattern", "r", encoding="utf8")
#Pattern="ribonucleoside-diphosphate reductase 1"
pattern = file2.read()
text = file1.read()


def search(pattern, text):
    if pattern == "":
        print("Pattern is empty")
        return -1

    patLen = len(pattern)
    textLen = len(text)
    patternMatch=0
    # create lps[] that will hold the longest prefix suffix
    # values for Longest_Pattern
    lps = [0] * patLen
    j = 0  # index for Longest_Pattern[]

    # Preprocess the Longest_Pattern (calculate lps[] array)
    computeLPSArray(pattern, patLen, lps)

    i = 0  # index for text[]
    while i < textLen:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == patLen:
            print("Found Pattern at index " + str(i - j))
            patternMatch+=1
            j = lps[j - 1]
            # mismatch after j matches
        elif i < textLen and pattern[j] != text[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    if patternMatch==0:
        print("Pattern not found in given text.")


def computeLPSArray(pattern, patLen, lps):
    length = 0  # length of the previous longest prefix suffix
    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < patLen:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


start_time = time.time()
search(pattern, text)
finish_time = time.time()
print("execution time %s" % (finish_time - start_time))