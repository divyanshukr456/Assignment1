n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

total = sum(arr)
average = total / n

print("Sum =", total)
print("Average =", average)