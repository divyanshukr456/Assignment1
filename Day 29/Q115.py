def str_ops():
    while True:
        print("\n1. Reverse String\n2. Convert to Uppercase\n3. Exit")
        c = input("Choice: ")
        if c == '1':
            s = input("String: ")
            print(s[::-1])
        elif c == '2':
            s = input("String: ")
            print(s.upper())
        elif c == '3': break
if __name__ == '__main__':
    str_ops()
