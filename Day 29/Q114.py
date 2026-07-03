def arr_ops():
    arr = []
    while True:
        print("\n1. Add Element\n2. Remove Element\n3. View Array\n4. Exit")
        c = input("Choice: ")
        if c == '1': arr.append(input("Element: "))
        elif c == '2':
            el = input("Element to remove: ")
            if el in arr: arr.remove(el)
            else: print("Not found.")
        elif c == '3': print(arr)
        elif c == '4': break
if __name__ == '__main__':
    arr_ops()
