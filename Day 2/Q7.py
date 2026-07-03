def product_of_digits(n):
    prod = 1
    for digit in str(abs(n)):
        prod *= int(digit)
    return prod
n = int(input("Enter number: "))
print("Product of digits:", product_of_digits(n))
