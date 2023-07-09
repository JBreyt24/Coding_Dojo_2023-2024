

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
		if (self.balance >= amount):
			self.balance -= amount
			return self
		else:
			self.balance -= 5.00
			print("\n Insufficient balance. A $5.00 charge will be processed.")
			return self

	def display_account_info(self):
		print("---------------------------")
		print(f"Balance = {self.balance}")
		print("---------------------------")
		return self

	def yield_interest(self):
		self.balance *= self.int_rate
		return self

	@classmethod
	def print_user_accounts(cls):
		for accounts in cls.accounts:
			accounts.display_account_info()

class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.account = BankAccount(int_rate=0.02, balance=0)


	def make_deposit(self, amount):
		self.account.deposit(amount)
		return self

	def make_withdrawal(self, amount):
		self.account.withdraw(amount)
		return self

	def display_user_balance(self):
		print(f"Account Balance = {self.account}")
		return self



user1 = User("Josh", "jbreyt24@gmail.com")
user2 = User("Reid", "palettesound@gmail.com")


print(user1.name)
user1.make_deposit(50).make_withdrawal(10).display_user_balance()

print(user2.name)
user2.make_deposit(100).make_withdrawal(30).make_withdrawal(50).display_user_balance()
