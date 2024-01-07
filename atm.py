import random

class BankAccount:
    def __init__(self, account_number, account_holder, pin, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN successfully changed.")

def authenticate(account):
    entered_pin = input("Enter your PIN: ")
    attempts = 3

    while entered_pin != account.pin and attempts > 0:
        print("Incorrect PIN. Please try again.")
        entered_pin = input("Enter your PIN: ")
        attempts -= 1

    if entered_pin == account.pin:
        return True
    else:
        print("Too many incorrect attempts. Exiting.")
        return False

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = random.randint(100000, 999999)
        account_holder = input("Enter your name: ")
        pin = input("Set your PIN: ")

        new_account = BankAccount(account_number, account_holder, pin)
        self.accounts[account_number] = new_account

        print(f"Account created successfully. Your account number is {account_number}.")

    def run(self):
        while True:
            print("\nATM Menu:")
            print("1. Create Account")
            print("2. Access Account")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                account_number = int(input("Enter your account number: "))
                if account_number in self.accounts:
                    account = self.accounts[account_number]
                    if authenticate(account):
                        self.perform_transaction(account)
                else:
                    print("Account not found. Please create an account.")
            elif choice == "3":
                print("Exiting ATM. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def perform_transaction(self, account):
        while True:
            print("\nTransaction Menu:")
            print("1. Display Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Logout")

            option = input("Enter your choice (1-5): ")

            if option == "1":
                account.display_balance()
            elif option == "2":
                amount = float(input("Enter the deposit amount: $"))
                account.deposit(amount)
            elif option == "3":
                amount = float(input("Enter the withdrawal amount: $"))
                account.withdraw(amount)
            elif option == "4":
                new_pin = input("Enter your new PIN: ")
                account.change_pin(new_pin)
            elif option == "5":
                print("Logging out. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
