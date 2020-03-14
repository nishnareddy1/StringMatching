import time

file1 = open(r"../A_tale_of_two_cities.txt", "r", encoding="utf8")
file2 = open(r"../Longest_Pattern", "r", encoding="utf8")
#pattern="bifunctional demethylmenaquinone methyltransferase/2-methoxy-6-polyprenyl-1,4-benzoquinol methylase"
pattern = file2.read()
text = file1.read()


def bruteSearch(pattern, text):
    # edge case check
    if pattern == "":
        print("Pattern is empty")
        return -1

    # length of text and Longest_Pattern
    patLen = len(pattern)
    textLen = len(text)
    patternMatch = 0
    # i is the index of text from where we will start comparing the Longest_Pattern
    i = 0
    # length of the subtext has to be equal to the length of the word,
    # so no need to check beyond (textLen - patLen + 1)
    while i < (textLen - patLen + 1):
        # we set match to false if we find a mismatch
        match = True

        for j in range(patLen):
            if pattern[j] != text[i + j]:
                # A mismatch
                match = False
                break

        if match:
            patternMatch += 1
            # We found a match at index i
            print("There is a match at " + str(i))
        # incrementing i is like shifting the word by 1
        i += 1
    if patternMatch==0:
        print("Pattern not found in given text.")
    return -1


start_time = time.time()
bruteSearch(pattern, text)
finish_time = time.time()
print("execution time %s" % (finish_time - start_time))