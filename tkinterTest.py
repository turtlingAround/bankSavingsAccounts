from tkinter import *

root = Tk()

def destroyWidgets():
    for widget in myframe.winfo_children():
        print(widget)

myframe = Frame(root,bg='#FF0000').pack()   

a = Button(root,text='Hello!',command=destroyWidgets).pack()
b = Label(root,text='label').pack()
aa = Button(myframe,text='Hello!',command=destroyWidgets,bg='#FF0000').pack()
bb = Label(myframe,text='label',bg='#FF0000').pack()

root.mainloop()