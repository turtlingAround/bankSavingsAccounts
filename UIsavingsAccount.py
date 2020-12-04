from savingaccount2 import SavingAccount
from customer import Customer

print('Hi there! Please enter with your customer pin to access the services \
\n(Or if you don\'t have a customer account, just press "Enter"). ')
pinFound = False
while not pinFound:
    pin = input('Pin: ')
    if not pin:
        name = input('Alright, please register by entering your name: ')
        a = Customer(name)
        accounts = []
        pinFound = True

    else:
        with open('customerInformation') as c:
            customers = c.read().split('\n')
        
        for item in customers:
            try:
                if pin == item.split(',')[1][:6]:
                    customerInfo = item.split('|')
                    customerAccountInfo = customerInfo[0].split(',')
                    accountNumbers = customerInfo[1:]
                    with open('savingAccountsinformation') as s:
                        l = s.read().split('\n')
                    accounts = []
                    for account in accountNumbers:
                        for item in l:
                            if account in item:
                                accounts.append(item)

                    a = Customer(customerAccountInfo[0],customerAccountInfo[1],False)
                    pinFound = True
                    break

            except IndexError:
                print('Sorry, please enter a valid pin.')


print("A: Create a new account \
\nB: Deposit money into an existing account \
\nC: Withdraw money from an existing account\
\nD: Transfer money from an account to another\n")

run = True
while run:
    option = input(f'Hello there, {a.name}. Please choose one of the options above: ').upper()

    if option == 'A':
        startingMoney = input('Alright, please enter the starting amount of money (in this format => $$.¢¢): ')
        new = a.newAccount(startingMoney)
        accounts.append(new)

    elif option == 'B':
        accountNumber = input('Please enter the number of the account you want to deposit into: ')
        balance = ''
        for account in accounts:
            if accountNumber in account:
                balance = account.split(',')[2]
                z = account

        if balance:
            balance = float(balance)
            depositAccount = SavingAccount(a.name,balance,a.pin,accountNumber,False)
            depositAmount = input('Alright, please enter the deposit amount (in this format => $$.¢¢): ')
            result = depositAccount.deposit(depositAmount)
            if result:
                balance += depositAmount
                accounts[accounts.index(z)].split(',')[2] = balance
                


        
        else:
            print('Please enter a valid account number.')


    elif option == 'C':
        accountNumber = input('Please enter the number of the account you want to withdraw from: ')
        balance = ''
        for account in accounts:
            if accountNumber in account:
                balance = account.split(',')[2]
                z = account

        if balance:
            balance = float(balance)
            withdrawAccount = SavingAccount(a.name,balance,a.pin,accountNumber,False)
            withdrawAmount = input('Alright, please enter the withdraw amount (in this format => $$.¢¢): ')
            result = withdrawAccount.withdraw(withdrawAmount)
            if result:
                balance -= withdrawAmount
                accounts[accounts.index(z)].split(',')[2] = balance
        
        else:
            print('Please enter a valid account number.')

    elif option == 'D':
        givingNumber = input('Please enter the number of the account you want to transfer from: ')
        receivingNumber = input('Please enter the number of the account you want to transfer to: ')
        givingBalance = ''
        receivingBalance = ''
        for account in accounts:
            if givingNumber in account:
                givingBalance = account.split(',')[2]
                givingZ = account
            elif receivingNumber in account:
                receivingBalance = account.split(',')[2]
                receivingZ = account

        if givingBalance and receivingBalance:
            givingBalance,receivingBalance = float(givingBalance),float(receivingBalance)
            givingAccount = SavingAccount(a.name,givingBalance,a.pin,givingNumber,False)
            receivingAccount = SavingAccount(a.name,receivingBalance,a.pin,receivingNumber,False)
            transferAmount = input('Alright, please enter the transfer amount (in this format => $$.¢¢): ')
            result = givingAccount.transfer(receivingAccount,transferAmount)
            if result:
                givingBalance -= transferAmount
                accounts[accounts.index(givingZ)].split(',')[2] = givingBalance

                receivingBalance += transferAmount
                accounts[accounts.index(receivingZ)].split(',')[2] = receivingBalance
        
        else:
            print('Please enter a valid account number.')

     
    elif option == '':
        print('Thanks! Have a nice day.')
        run = False

    
    else:
        print('Please enter a valid option.')


        '''elif option == 'D':
        givingNumber = input('Please enter the number of the account you want to transfer from: ')
        receivingNumber = input('Please enter the number of the account you want to transfer to: ')
        givingBalance = ''
        receivingBalance = ''
        for account in accounts:
            if givingNumber in account:
                givingBalance = account.split(',')[2]
            elif receivingNumber in account:
                receivingBalance = account.split(',')[2]

        if givingBalance and receivingBalance:
            givingAccount = SavingAccount(a.name,givingBalance,a.pin,givingNumber,False)
            receivingAccount = SavingAccount(a.name,receivingBalance,a.pin,receivingNumber,False)
            transferAmount = input('Alright, please enter the transfer amount (in this format => $$.¢¢): ')
            givingAccount.transfer(receivingAccount,transferAmount)
        
        else:
            print('Please enter valid account numbers.')
'''
       