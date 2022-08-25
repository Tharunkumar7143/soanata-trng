from account import Account

def withdraw(balance,amount):
    if(balance < amount):
        raise"not suffient balance"
    balance=balance-amount