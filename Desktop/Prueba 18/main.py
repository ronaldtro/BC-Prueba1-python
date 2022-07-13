
import tkinter

window = tkinter.Tk()

seleccionado = tkinter.StringVar() #Intvar..
seleccionado.set('0')

def clickButton(event):
    seleccionado.set('0')

r1 = tkinter.Radiobutton(window, text='Opcion 1', value='1', variable=seleccionado)
r2 = tkinter.Radiobutton(window, text='Opcion 2', value='2', variable=seleccionado)
r3 = tkinter.Radiobutton(window, text='Opcion 3', value='3', variable=seleccionado)
l1 = tkinter.Label(window, textvariable=seleccionado)
b1 = tkinter.Button(window, text='Reiniciar')


b1.bind('<Button-1>', clickButton)


r1.grid(row=0, column=0, padx=5, pady=5)
r2.grid(row=1, column=0, padx=5, pady=5)
r3.grid(row=2, column=0, padx=5, pady=5)
l1.grid(row=3, column=0, sticky="E", padx=40)
b1.grid(row=4, column=0, padx=5, pady=5)


window.mainloop()