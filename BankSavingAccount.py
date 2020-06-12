from random import randint
from savingaccount import SavingAccount

class BankSavingAccounts:
    def __init__(self,bankName,accounts):
        self.bankName = bankName
        self.accounts = accounts
        self.numberOfAccounts = len(accounts)

    def changeInterest(self,changeAmount):
        decimalCount = len(str(changeAmount)) - 1
        SavingAccount.interestRate = round(SavingAccount.interestRate + changeAmount,decimalCount)
