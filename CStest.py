from tkinter import *
from savingaccount2 import SavingAccount
from customer import Customer

from OS import openingScreen

root = Tk('600x600')
def CS():
    def option1():
        print('3240872570')
    CS = Frame()
    CS.pack()

    create = PhotoImage(file='create.png')
    deposit = PhotoImage(file='deposit.png')
    withdraw = PhotoImage(file='withdraw.png')
    transfer = PhotoImage(file='transfer.png')

    CSlabel = Label(CS, text = f'Hello there. Please choose one of the options below: ')
    CSlabel.grid(columnspan = 2)

    CSop1 = Button(CS,text='Create Account',image=create,compound=TOP,command=option1).grid(row=1, column=0)

    CSop2 = Button(CS,text='Deposit Money',image=deposit,compound=TOP).grid(row=1, column=1)

    CSop3 = Button(CS,text='Withdraw Money',image=withdraw,compound=TOP).grid(row=2, column=0)

    CSop4 = Button(CS,text='Transfer Money',image=transfer,compound=TOP).grid(row=2, column=1)
CS()
#ChoosingScreen()
root.mainloop()