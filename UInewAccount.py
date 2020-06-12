from savingaccount import SavingAccount

#check for legitimate starting amount
def legitimateStartingAmount(startingAmount):
    try:
        if float(startingAmount) < 0:
            return False
    except:
        return False
    if '.' in startingAmount:
        decimalCount = len(startingAmount[startingAmount.index('.') + 1:])
        if decimalCount > 2:
            return False
    return True
     

print("A: Create a new account \
    \nB: Deposit money into an existing account \
    \nC: Withdraw money from an existing account\n")

run = True
while True:
    option = input('\nPlease enter an option: ')

    if option.upper() == 'A':
        customerName = input('Alright, please enter your name: ')
        startingAmount = input('Please enter the starting amount: ')


        if legitimateStartingAmount(startingAmount):
            SA = SavingAccount(customerName,float(startingAmount))
        
            print('Alright, the new account has been created!')
            print(SA)

        else:
            print('Please enter a valid amount.')


    elif option.upper() == 'B':
        accountNumber = input('Please enter your account number: ').zfill(5)
        try:

            with open('bankSavingsAccounts/savingAccountsinformation','r') as s:
                lines = s.read().split('\n')
            for item in lines:
                if accountNumber in item:
                    depositAmount = input('Please enter the amount of money you want to deposit in dollars (in this format ==> $$.¢¢): ')
                    if legitimateStartingAmount(depositAmount):
                        depositAmount = float(depositAmount)

                        info = item.split(',')
                        validOp = True
                        break

                    else:
                        print('Please enter a valid amount.')
                        validOp = False
                        break

                elif lines.index(item) + 1 == len(lines):
                    print('Please enter a valid account number.')
                    validOp = False
            
            if validOp:
                a = SavingAccount(info[0],float(info[2]),info[1],True)
                a.deposit(depositAmount)

                print('Alright, the money has been deposited!')
        except TypeError:
            print('Please enter a valid amount of money.')


    elif option.upper() == 'C':
        accountNumber = input('Please enter your account number: ').zfill(5)
        try:

            with open('bankSavingsAccounts/savingAccountsinformation','r') as s:
                lines = s.read().split('\n')
            for item in lines:
                if accountNumber in item:
                    depositAmount = input('Please enter the amount of money you want to deposit in dollars (in this format ==> $$.¢¢): ')
                    if legitimateStartingAmount(depositAmount):
                        depositAmount = float(depositAmount)

                        info = item.split(',')
                        validOp = True
                        break

                    else:
                        print('Please enter a valid amount.')
                        validOp = False
                        break

                elif lines.index(item) + 1 == len(lines):
                    print('Please enter a valid account number.')
                    validOp = False
            
            if validOp:
                a = SavingAccount(info[0],float(info[2]),info[1],True)
                a.deposit(depositAmount)

                print('Alright, the money has been deposited!')
        except TypeError:
            print('Please enter a valid amount of money.')       

    elif option == '':
        print('Thank you, have a nice day! :)')
        exit()

    else:
        print('Sorry, please enter a valid option.')