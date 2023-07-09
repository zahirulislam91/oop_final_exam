

class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0
        self.loan_amount = 0
        self.transaction_history = []
        self.loan_feature_enabled = True
        
        print(f"User Name: {self.name}")
        print(f"User Email: {self.email}")
        print(f"User Password: {self.password}")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: {amount}")
        else:
            print("Insufficient balance. Unable to withdraw.")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transfer: {amount} to {recipient.name}")
            recipient.transaction_history.append(f"Transfer: {amount} from {self.name}")
        else:
            print("Insufficient balance. Unable to transfer.")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history
    
    def loan(self, is_enabled) :
        self.loan_enabled = is_enabled
        if is_enabled:
            loan_limit = self.balance * 2
            self.balance += loan_limit
            self.loan_amount += loan_limit
            self.transaction_history.append(f"Loan taken: {loan_limit}")
            print("Loan enabled.")
        else:
            print("Loan disabled.")



    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}"


class Admin(User):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
    
        print(f"Admin Name: {self.name}")
        print(f"Admin Email: {self.email}")
        print(f"Admin Password: {self.password}")

    def check_total_balance(self, users):
        total_balance = sum(user.balance + user.loan_amount for user in users)
        return total_balance

    def check_total_loan_amount(self, users):
        total_loan_amount = sum(user.loan_amount for user in users)
        return total_loan_amount



user1 = User("Karim Ullah", "karim@ullah.com", "123456")
user2 = User("Rahim Ullah", "user2@ullah.com", "654321")
admin = Admin("Dr. Shahid", "shahid@bb.com", "1472583")

user1.deposit(1000)
user1.withdraw(50)
user1.transfer(150, user2)
user1.loan(True)

print(user1.check_transaction_history())
print(f"Current balance: {user1.check_balance()}")
print(f"Admin loan: {admin.loan(False)}")
