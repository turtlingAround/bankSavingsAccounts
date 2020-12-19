from tkinter import *
from savingaccount2 import SavingAccount
from customer import Customer

#Choosing Screen
def choosingScreen(a, accounts):
    a, accounts = a, accounts
    a = openingScreen()
    OS.pack_forget()

    #createAcc
    def option1():
        def createNotification():
            createMessage = messagebox.showinfo(title='Confirmation',message=f'Alright, a new savings account has been formed!')
            createMessage.pack()
        
        CS.pack_forget()

        create = Frame()
        create.pack()

        createLabel = Label(create, text= 'Alright, please enter the starting amount of money (in this format => $$.¢¢):')
        createLabel.pack()

        createEntry = Entry(create)
        createEntry.insert(END,'Starting money')
        createEntry.pack()

        createButton = Button(create,text = 'Enter',highlightbackground = 'green',padx=5, pady=5)
        createButton.pack()

    def option1():
        print('328752057')
    CS = Frame()
    CS.pack()

    create = PhotoImage(file='create.png')
    deposit = PhotoImage(file='deposit.png')
    withdraw = PhotoImage(file='withdraw.png')
    transfer = PhotoImage(file='transfer.png')

    CSlabel = Label(CS, text = f'Hello there. Please choose one of the options below: ')
    CSlabel.grid(columnspan = 2)

    CSop1 = Button(CS,text='Create Account',image=create,compound=TOP, command= option1).grid(row=1, column=0)

    CSop2 = Button(CS,text='Deposit Money',image=deposit,compound=TOP).grid(row=1, column=1)

    CSop3 = Button(CS,text='Withdraw Money',image=withdraw,compound=TOP).grid(row=2, column=0)

    CSop4 = Button(CS,text='Transfer Money',image=transfer,compound=TOP).grid(row=2, column=1)

#openingScreen
def openingScreen():
    global OS
    OS = Frame()
    OS.pack()
    def newCustomer():
        a = accounts = None
        NC = Frame()
        NC.pack()

        def back():
            NC.pack_forget()
            NCquit.pack_forget()
            NCbutton.pack_forget()
            OS.pack()
            return

        def new():
            name= NCentry.get()
            a = Customer(name)
            accounts = []
            NCmessage = messagebox.showinfo(title='Confirmation',message=f'Alright, a new customer account has been formed!\n   name: {a.name}\n   pin: {a.pin}\nNote: Your pin is very important. Do not share it with anybody.\n')
            return a, accounts

        NCbutton = Button(text='Enter', command=new)
        NCbutton.pack()

        NClabel= Label(NC,text='Please register by entering your name.')
        NClabel.pack()

        NCentry = Entry(NC)
        NCentry.insert(END,'name')
        NCentry.pack()

        NCquit = Button(text='Back', command=back)
        NCquit.pack()

    def NCframeAll():
        OS.pack_forget()
        newCustomer()
        
    def getPIN(pin):
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
                    OS.pack_forget()
                    choosingScreen(a, accounts)

            except IndexError:
                OSinvalidPIN = Label(OS,text = 'Sorry, please enter a valid pin.',fg = 'red')
                OSinvalidPIN.grid(row = 5, sticky = E)


    OSname = Label(OS,fg = 'purple',font=('Verdana','24'),text = 'ABC BANK Savings Accounts')
    OSname.grid(row = 0, column = 0)

    OSlabel = Label(OS,fg = 'blue',text = '\n\nPlease log in with your customer PIN\n')
    OSlabel.grid(row = 1, column = 0,sticky = EW)

    OSPIN = Entry(OS)
    OSPIN.insert(END,'enter PIN')
    OSPIN.grid(row = 2, column = 0)

    OSenter = Button(OS,text = 'Enter',highlightbackground = 'green',padx = 5, pady = 5,command = lambda: getPIN(OSPIN.get()))
    OSenter.grid(row = 3, column = 0)

    OSnoAcc = Button(OS,text = '\n\nOr if you don\'t have a customer account, press here".',command= NCframeAll)
    OSnoAcc.grid(row = 4,column = 0, sticky = EW)

root = Tk('600x600')
choosingScreen(1,2)

#ChoosingScreen()
root.mainloop()