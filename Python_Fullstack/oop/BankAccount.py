



# class BankAccount:

# 	accounts = []

# 	def __init__(self, int_rate, balance):
# 		self.int_rate = int_rate
# 		self.balance = balance

# 		BankAccount.accounts.append(self)

# 	def deposit(self, amount):
# 		self.balance += amount
# 		return self

# 	def withdraw(self, amount):
# 		if (self.balance >= amount):
# 			self.balance -= amount
# 			return self
# 		else:
# 			self.balance -= 5.00
# 			print("\n Insufficient balance. A $5.00 charge will be processed.")
# 			return self

# 	def display_account_info(self):
# 		print("---------------------------")
# 		if (self.balance < 0):
# 			print(f"Balance = {self.balance}")
# 		else:
# 			print(f"Balance = {self.balance}")
# 		print("---------------------------")
# 		return self

# 	def yield_interest(self):
# 		self.balance *= self.int_rate
# 		return self


# user1 = BankAccount(int_rate = 0.05, balance = 100.00)
# user1.withdraw(110.00).display_account_info()

# user1 = BankAccount(int_rate = 0.05, balance = 0.00)
# user1.deposit(10.00).deposit(20.00).deposit(30.00).withdraw(10.00).display_account_info()


# user2 = BankAccount(int_rate = 0.05, balance = 20.00)
# user2.deposit(20.00).deposit(20.00).withdraw(5.00).withdraw(20.00).withdraw(20.00).withdraw(20.00).display_account_info()



class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5.00
            print("\nInsufficient balance. A $5.00 charge will be processed.")
        return self

    def display_account_info(self):
        print("---------------------------")
        if self.balance < 0:
            print(f"Balance = -${-self.balance:.2f}")
        else:
            print(f"Balance = ${self.balance:.2f}")
        print("---------------------------")
        return self

    def yield_interest(self):
        self.balance *= self.int_rate
        return self


user1 = BankAccount(int_rate=0.05, balance=100.00)
user1.withdraw(110.00)
user1.display_account_info()