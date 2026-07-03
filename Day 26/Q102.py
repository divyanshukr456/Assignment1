def voting_eligibility():
    try:
        age = int(input("Enter your age: "))
        if age >= 18:
            print("You are eligible to vote.")
        elif age > 0:
            print(f"You will be eligible to vote in {18 - age} years.")
        else:
            print("Invalid age entered.")
    except ValueError:
        print("Please enter a valid number.")
if __name__ == '__main__':
    voting_eligibility()
