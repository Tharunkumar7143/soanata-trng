class Account:

    def __init__(self,acno,acname,atype,bal):
        self.accountnumber=acno
        self.accountname=acname
        self.accounttype=atype
        self.balance=bal

    def display(self):
        return self.acno + self.acname + self.atype + self.bal
