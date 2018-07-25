from tkinter import *

root = Tk()
#Make a square where to write in.
inc = Entry(root)
inc.pack()
#Write text into the field to explain what value to put in.
inc.delete(0, END)
inc.insert(0, "Inkomst")
inc.focus_set()

#Make a square where to write in.
eq = Entry(root)
eq.pack()
#Write text into the field to explain what value to put in.
eq.delete(0, END)
eq.insert(0, "Egen insats")
eq.focus_set()

#Make a square where to write in.
stock = Entry(root)
stock.pack()
#Write text into the field to explain what value to put in.
stock.delete(0, END)
stock.insert(0, "Aktier")
stock.focus_set()

def callback():
    print (inc.get())
    print (eq.get())
    print (stock.get())
    

b = Button(root, text="Print", width=10, command=callback)
b.pack()

mainloop()


root.mainloop()


