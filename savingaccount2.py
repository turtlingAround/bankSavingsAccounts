from random import randint
from legitimateDWT import LegitimateDWT

class SavingAccount:
    def __init__(self,customerName,startingMoney,customerPin,accountNumber = '',newAccount = True):
        self.customerName = customerName
        self.total = startingMoney
        if LegitimateDWT(startingMoney):
            self.total = startingMoney

            self.accountNumber = accountNumber
            self.customerPin = customerPin

            if newAccount:
                with open('bankSavingsAccounts/savingAccountsinformation','r') as s:
                    a = s.read().split(',')
                taken = [a[i] for i in range(len(a)) if i % 4 == 1]

                while self.accountNumber in taken or not self.accountNumber:
                    self.accountNumber = str(randint(1,99999))
                self.accountNumber = self.accountNumber.zfill(5)

                with open('bankSavingsAccounts/savingAccountsinformation','a') as s:
                    s.write(self.__str__())
                    print(f'Alright, a new savings account has been formed!\n    {self.__str__()}')
        else:
            print('Please enter a valid starting amount.')
            run = False


    def deposit(self,depositAmount):
        if LegitimateDWT(depositAmount):
            self.total += round(float(depositAmount),2)

            with open('bankSavingsAccounts/SavingAccountsinformation','r') as t:
                lines = t.readlines()
            for item in lines:
                if self.accountNumber in item:
                    info = item.split(',')
                    lines[lines.index(item)] = self.__str__()

                    print(f'Alright, the money has been deposited!\n    {self.__str__()}')

            with open('bankSavingsAccounts/SavingAccountsinformation','w') as t:
                for item in lines:
                    t.write(item)

        else:
            print('Sorry, please enter a valid deposit amount.' )


    def withdraw(self,withdrawAmount):
        if LegitimateDWT(withdrawAmount):
            self.total -= round(float(withdrawAmount),2)

            with open('bankSavingsAccounts/SavingAccountsinformation','r') as t:
                lines = t.readlines()
            for item in lines:
                if self.accountNumber in item:
                    info = item.split(',')
                    lines[lines.index(item)] = self.__str__()

                    print(f'Alright, the money has been withdrawn!\n    {self.__str__()}')

            with open('bankSavingsAccounts/SavingAccountsinformation','w') as t:
                for item in lines:
                    t.write(item)

        else:
            print('Sorry, please enter a valid withdrawal amount.' )


    def transfer(self,receivingAccount,transferAmount):
        if LegitimateDWT(transferAmount):
            transferAmount = float(transferAmount)
            if self.total > transferAmount:
                self.total -= transferAmount
                receivingAccount.total -= transferAmount

                with open('bankSavingsAccounts/SavingAccountsinformation','r') as t:
                    lines = t.readlines()
                for item in lines:
                    if self.accountNumber in item:
                        info = item.split(',')
                        lines[lines.index(item)] = self.__str__()

                    if receivingAccount.accountNumber in item:
                        info = item.split(',')
                        lines[lines.index(item)] = self.__str__()

                        print(f'Alright, the money has been transferred!\
                            \n  Providing account: {self.__str__()}\n   Receiving account: {receivingAccount.__str__()}')

                with open('bankSavingsAccounts/SavingAccountsinformation','w') as t:
                    for item in lines:
                        t.write(item)

        else:
            print('Sorry, please enter a valid transfer amount.' )


    def __str__(self):
        return f'{self.customerName},{self.accountNumber},{self.total},{self.customerPin}\n'