from abc import ABC, abstractmethod

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.atms = []
    
    def add_customer(self, customer):
        self.customers.append(customer)
    
    def add_atm(self, atm):
        self.atms.append(atm)

class ATM:
    def __init__(self, atm_id, location):
        self.atm_id = atm_id
        self.location = location
    
    def authenticate_customer(self, customer_id):
        print(f"Customer {customer_id} authenticated")
    
    def process_transaction(self, transaction_id):
        print(f"Transaction {transaction_id} processed")

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)

class ATMTransaction:
    def __init__(self, transaction_id, amount, transaction_type, date, account):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date
        self.account = account


class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    def get_balance(self):
        return self.balance

class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def deposit(self, amount):
        pass  # Mocked method
    
    def withdraw(self, amount):
        pass  # Mocked method

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        pass  # Mocked method
    
    def withdraw(self, amount):
        pass  # Mocked method
