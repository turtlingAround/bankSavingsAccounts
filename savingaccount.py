from random import randint

class SavingAccount:
    interestRate = 0.05

    def __init__(self,customerName,startingMoney,accountNumber = '',depositOrWithdraw = False):
        self.customerName = customerName
        self.total = startingMoney
        if not depositOrWithdraw:
            with open('bankSavingsAccounts/savingAccountsinformation','r') as s:
                a = s.read().split(',')
            taken = [a[i] for i in range(len(a)) if i % 3 == 1]

            while accountNumber in taken or not accountNumber:
                accountNumber = str(randint(1,99999))
            accountNumber = accountNumber.zfill(5)

        self.accountNumber = accountNumber

        if not depositOrWithdraw:
            with open('bankSavingsAccounts/savingAccountsinformation','a') as s:
                s.write(self.__str__())

    def deposit(self,depositAmount):
        if depositAmount < 0:
            print('Sorry, please enter a valid deposit amount.')
        else:

            with open('bankSavingsAccounts/SavingAccountsinformation','r') as t:
                lines = t.readlines()
            for item in lines:
                if self.accountNumber in item:
                    info = item.split(',')
                    self.total += depositAmount
                    print(self.__str__())
                    lines[lines.index(item)] = self.__str__()

                elif lines.index(item) == len(lines):
                    print('Sorry, please enter a valid account number.')

            with open('bankSavingsAccounts/SavingAccountsinformation','w') as t:
                for item in lines:
                    t.write(item)

    def withdraw(self,withdrawAmount):
        if withdrawAmount < 0:
            print('Sorry, please enter a valid deposit amount.')
            
        
        else:

            with open('bankSavingsAccounts/SavingAccountsinformation','r') as t:
                lines = t.readlines()
            for item in lines:
                if accountNumber in item:
                    info = item.split(',')
                    self.total -= depositAmount
                    lines[lines.index(item)] = self.__str__()

                elif lines.index(item) == len(lines):
                    print('Sorry, please enter a valid account number.')

            with open('bankSavingsAccounts/SavingAccountsinformation','w') as t:
                for item in lines:
                    t.write(item)



    def transfer(self,receivingAccount,transferAmount):
        pass
    def passYear(self,currentDate):
        self.total += self.total * self.interestRate / 100

    def __str__(self):
        return f'{self.customerName},{self.accountNumber},{self.total:.2f}\n'