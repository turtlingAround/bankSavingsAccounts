from tkinter import *
root = Tk('600x600')

deposit = Frame()
deposit.pack()

accNumLabel = Label(deposit, text= 'Please enter the number of the account you want to deposit into:')
accNumLabel.pack()

accNumbEntry = Entry(deposit)
accNumEntry.insert(END,'Account Number')
accNumEntry.pack()

accNumButton = Button(create,text = 'Enter',highlightbackground = 'green',padx=5, pady=5)
accNumButton.pack()

root.mainloop()