inventory = {}
def inv_system():
    while True:
        print("\n1. Add Item\n2. Update Stock\n3. View Inventory\n4. Exit")
        c = input("Choice: ")
        if c == '1':
            item = input("Item name: ")
            qty = int(input("Quantity: "))
            inventory[item] = qty
        elif c == '2':
            item = input("Item name: ")
            if item in inventory:
                inventory[item] += int(input("Quantity to add: "))
        elif c == '3':
            for i, q in inventory.items(): print(f"{i}: {q}")
        elif c == '4': break
if __name__ == '__main__':
    inv_system()
