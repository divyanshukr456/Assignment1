def is_palindrome(n):
    s = str(abs(n))
    return s == s[::-1]
n = int(input("Enter number: "))
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not a palindrome")
