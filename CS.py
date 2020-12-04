from tkinter import *
from savingaccount2 import SavingAccount
from customer import Customer

'''from OS import openingScreen
from NC import newCustomer'''

root = Tk('600x600')

CS = Frame(root)
CS.pack()

create = PhotoImage(file='add.png')
deposit = PhotoImage(file='bank.png')
withdraw = PhotoImage(file='bank (1).png')
transfer = PhotoImage(file='bank-transfer.png')

CSlabel = Label(CS, text = f'Hello there. Please choose one of the options below: ')
CSlabel.grid(columnspan = 2)

CSop1 = Button(CS,text='Create Account',image=create,compound=TOP).grid(row=1, column=0)
CSop1.pack()
CSop2 = Button(CS,text='Deposit Money',image=deposit,compound=TOP).grid(row=1, column=1)
CSop2.pack()
CSop3 = Button(CS,text='Withdraw Money',image=withdraw,compound=TOP).grid(row=2, column=0)
CSop3.pack()
CSop4 = Button(CS,text='Transfer Money',image=transfer,compound=TOP).grid(row=2, column=1)
CSop4.pack()

root.mainloop()