def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = int(str(n)[::-1])
    return rev * sign
n = int(input("Enter number: "))
print("Reversed number:", reverse_number(n))
