
class User:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

class ATM:
    def __init__(self):
        self.users = {}  # Simulating a database of users

    def add_user(self, account_number, pin, balance):
        self.users[account_number] = User(account_number, pin, balance)

    def authenticate(self, account_number, pin):
        user = self.users.get(account_number)
        if user and user.pin == pin:
            return user
        return None

    def display_menu(self):
        print("\nOptions:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Exit")

    def process_transaction(self, user):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Your balance is: ${user.balance}")
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                if amount <= user.balance:
                    user.balance -= amount
                    print(f"Withdrawal successful. Remaining balance: ${user.balance}")
                else:
                    print("Insufficient funds.")
            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                user.balance += amount
                print(f"Deposit successful. New balance: ${user.balance}")
            elif choice == "4":
                print("Thank you for using the ATM!")
                break
            else:
                print("Invalid option. Please try again.")

# Simulating the ATM system
atm = ATM()
atm.add_user("123456", "1234", 1000)

account_number = input("Enter account number: ")
pin = input("Enter PIN: ")

user = atm.authenticate(account_number, pin)
if user:
    print("Login successful!")
    atm.process_transaction(user)
else:
    print("Invalid account number or PIN.")


