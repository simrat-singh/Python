import string, sys
def ispangram(str1):
    alphabet_set = set(string.ascii_lowercase)
    return alphabet_set <= set(str1.lower())

print(ispangram(input("Enter the String:")))


#Test case
#Enter string "The quick brown fox jumps over the lazy dog"