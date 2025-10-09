import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds


@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
(2, 3, 5),
(-1, 1, 0),
 (0, 0, 0)
])
def test_add(num1, num2, expected):
    print("Testing add function...")
    assert add(num1, num2) == expected


def test_subtract():
    print("Testing subtract function...")
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0 

def test_multiply():
    print("Testing multiply function...")
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0

def test_divide():
    print("Testing divide function...")
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(1, 0) == "Error: Division by zero"


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_initial_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    print("Testing withdraw method...")
    bank_account.withdraw(50)
    assert bank_account.balance == 0

def test_deposit(bank_account):
    print("Testing deposit method...")
    bank_account.deposit(50)
    assert bank_account.balance == 100

def test_collect_interest(bank_account):
    print("Testing collect_interest method...")
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55


@pytest.mark.parametrize("deposited, withdraw, expected", [
(200, 100, 100),
(50, 10, 40),
 (1200, 200, 1000)
])
def test_bank_transaction(zero_bank_account, deposited, withdraw, expected):
    print("Testing multiple transactions...")
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)