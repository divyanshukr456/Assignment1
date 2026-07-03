def check_rotation(s1, s2):
    if len(s1) != len(s2): return False
    temp = s1 + s1
    return s2 in temp
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if check_rotation(s1, s2):
    print("Strings are rotations")
else:
    print("Strings are not rotations")
