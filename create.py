from tkinter import *
root = Tk('600x600')
def createAcc():
    def createNotification():
        createMessage = messagebox.showinfo(title='Confirmation',message=f'Alright, a new savings account has been formed!')
        createMessage.pack()
    create = Frame()
    create.pack()

    createLabel = Label(create, text= 'Alright, please enter the starting amount of money (in this format => $$.¢¢):')
    createLabel.pack()

    createEntry = Entry(create)
    createEntry.insert(END,'Starting money')
    createEntry.pack()

    createButton = Button(create,text = 'Enter',highlightbackground = 'green',padx=5, pady=5)
    createButton.pack()

root.mainloop()