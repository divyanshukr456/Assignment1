def calc():
    while True:
        print("\n1. Add\n2. Sub\n3. Mul\n4. Div\n5. Exit")
        c = input("Choice: ")
        if c == '5': break
        a, b = float(input("A: ")), float(input("B: "))
        if c == '1': print(a + b)
        elif c == '2': print(a - b)
        elif c == '3': print(a * b)
        elif c == '4': print(a / b if b != 0 else "Cannot divide by 0")
if __name__ == '__main__':
    calc()
