from tkinter import *
from tkinter import messagebox
from savingaccount2 import SavingAccount
from customer import Customer

from CS import ChoosingScreen

root = Tk('600x600')

from time import sleep

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
                    ChoosingScreen()
                    break

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


    


openingScreen()

root.mainloop()