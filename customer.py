from savingaccount2 import SavingAccount
from random import randint

class Customer:
    def __init__(self,name,pin = '',newCustomer = True):
        self.name = name
        self.pin = pin

        if newCustomer:
            with open('customerInformation','r') as s:
                a = s.read().split(',')
            taken = [a[i] for i in range(len(a)) if i % 3 == 1]

            while self.pin in taken or not self.pin:
                self.pin = str(randint(1,999999))
            self.pin = self.pin.zfill(6)

            with open('customerInformation','a') as s:
                s.write(self.__str__())

                

    def newAccount(self,startingMoney):
        a = SavingAccount(self.name,startingMoney,self.pin)
        try:
            with open('customerInformation','r') as s:
                lines = s.read().split('\n')
                lines = [item for item in lines if item]
            
            for item in lines:
                if self.pin in item:
                    lines[lines.index(item)] += f'|{a.accountNumber}'

            with open('customerInformation','w') as s:
                for item in lines:
                    s.write(item)
                    s.write('\n')
        except:
            pass

    def __str__(self):
        return f'{self.name},{self.pin}\n'