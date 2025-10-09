def add(num1: int, num2: int):
    return num1 + num2

def subtract(num1: int, num2: int):
    return num1 - num2

def multiply(num1: int, num2: int):
    return num1 * num2  

def divide(num1: int, num2: int):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

class InsufficientFunds(Exception):
    pass

class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds")
        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1