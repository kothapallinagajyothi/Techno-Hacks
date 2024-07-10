class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is: ₹{self.balance:.2f}"

    def deposit(self, amount):
        self.balance += amount
        return f"₹{amount:.2f} deposited successfully. Your new balance is: ₹{self.balance:.2f}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds. Withdrawal failed."
        else:
            self.balance -= amount
            return f"₹{amount:.2f} withdrawn successfully. Your new balance is: ₹{self.balance:.2f}"

def main():
    print("Welcome to the ATM Simulator!")
    initial_balance = float(input("Enter your initial balance in ₹: "))
    atm = ATM(initial_balance)

    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print(atm.check_balance())
        elif choice == 2:
            amount = float(input("Enter the deposit amount in ₹: "))
            print(atm.deposit(amount))
        elif choice == 3:
            amount = float(input("Enter the withdrawal amount in ₹: "))
            print(atm.withdraw(amount))
        elif choice == 4:
            print("Exiting ATM Simulator. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()