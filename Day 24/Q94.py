def compress_string(s):
    if not s: return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    res = "".join(compressed)
    return res if len(res) < len(s) else s
s = input("Enter string: ")
print("Compressed string:", compress_string(s))
