from tkinter import *

ventana = Tk()
elemento = StringVar()

listbox = Listbox(ventana)

for elem in ['Ronald', 'Castro', 'Torres']:
 listbox.insert(END, elem)

label = Label(text="Lista")

label.pack()
listbox.pack()

ventana.mainloop()