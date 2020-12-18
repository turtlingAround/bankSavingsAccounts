from tkinter import *
root = Tk('600x600')

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