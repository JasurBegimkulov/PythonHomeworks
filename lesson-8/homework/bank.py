class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_string(self):
        return f"{self.account_number},{self.name},{self.balance}"

    @staticmethod
    def from_string(data):
        account_number, name, balance = data.split(",")
        return Account(int(account_number), name, float(balance))

class Bank:
    def __init__(self):
        self.accounts = {}
        self.file_name = "accounts.txt"
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        if initial_deposit < 0:
            print("Initial deposit must be non-negative.")
            return

        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Your account number is {account_number}.")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}\nName: {account.name}\nBalance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
            print(f"Deposited {amount}. New balance: {account.balance}.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        account = self.accounts.get(account_number)
        if account:
            if amount > account.balance:
                print("Insufficient funds.")
            else:
                account.balance -= amount
                self.save_to_file()
                print(f"Withdrew {amount}. New balance: {account.balance}.")
        else:
            print("Account not found.")

    def save_to_file(self):
        with open(self.file_name, "w") as f:
            for account in self.accounts.values():
                f.write(account.to_string() + "\n")

    def load_from_file(self):
        try:
            with open(self.file_name, "r") as f:
                for line in f:
                    account = Account.from_string(line.strip())
                    self.accounts[account.account_number] = account
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            account_number = int(input("Enter account number: "))
            bank.view_account(account_number)

        elif choice == "3":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == "4":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == "5":
            print("Thank you for using the banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
