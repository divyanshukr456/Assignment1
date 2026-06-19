n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

largest = max(arr)
smallest = min(arr)

print("Largest element =", largest)
print("Smallest element =", smallest)