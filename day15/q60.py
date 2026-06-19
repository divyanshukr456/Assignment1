arr = list(map(int, input("Enter elements: ").split()))

result = []

for num in arr:
    if num != 0:
        result.append(num)

zero_count = len(arr) - len(result)

for i in range(zero_count):
    result.append(0)

print("Array after moving zeroes:", result)