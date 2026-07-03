def atm_simulation():
    balance = 1000
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Select option: ")
        if choice == '1':
            print(f"Current Balance: ${balance}")
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print(f"Deposited: ${amount}")
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawn: ${amount}")
            else:
                print("Insufficient balance.")
        elif choice == '4':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option.")
if __name__ == '__main__':
    atm_simulation()
