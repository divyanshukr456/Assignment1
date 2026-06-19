n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

print("Array elements are:")
for i in arr:
    print(i, end=" ")