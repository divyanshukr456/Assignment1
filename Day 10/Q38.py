def print_reverse_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
n = int(input("Enter number of rows: "))
print_reverse_pyramid(n)
