from tkinter import *
from tkinter import messagebox
from savingaccount2 import SavingAccount
from customer import Customer

def newCustomer():
    a = accounts = None
    NC = Frame()
    NC.pack()

    def back():
        NC.pack_forget()
        NCquit.pack_forget()
        OS.pack()
        return

    def new():
        name= NCentry.get()
        a = Customer(name)
        accounts = []
        NCmessage = messagebox.showinfo('Confirmation',f'Alright, a new customer account has been formed!\n   name: {a.name}\n   pin: {a.pin}\nNote: Your pin is very important. Do not share it with anybody.\n')
        return a, accounts


    NClabel= Label(NC,text='Please register by entering your name.')
    NClabel.pack()

    NCentry = Entry(NC)
    NCentry.insert(END,'name')
    NCentry.pack()

    NCquit = Button(text='Back', command=back)
    NCquit.pack()

    NCbutton = Button(text='Enter', command=new)
    NCbutton.pack()