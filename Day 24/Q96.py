def remove_duplicates(s):
    seen = set()
    res = []
    for char in s:
        if char not in seen:
            seen.add(char)
            res.append(char)
    return "".join(res)
s = input("Enter string: ")
print("String without duplicates:", remove_duplicates(s))
