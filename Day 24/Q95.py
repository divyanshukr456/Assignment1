def longest_word(s):
    words = s.split()
    if not words: return ""
    return max(words, key=len)
s = input("Enter sentence: ")
print("Longest word:", longest_word(s))
