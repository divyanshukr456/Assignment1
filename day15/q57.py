arr = list(map(int, input("Enter elements: ").split()))

reversed_arr = arr[::-1]

print("Reversed Array:", reversed_arr)

#without slicing
arr = list(map(int, input().split()))

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")