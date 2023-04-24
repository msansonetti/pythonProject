import tkinter

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

lista = ['Azul', 'Rojo', 'Negro', 'Verde', 'Blanco', 'Amarillo']
lista_items = tkinter.StringVar(value=lista)

list_box = tkinter.Listbox(window, height=20, listvariable=lista_items)
list_box.grid(column=0, row=0, sticky=tkinter.W)

label_color = tkinter.Label(window, text='Selección de colores')
label_color.grid(column=0, row=1, sticky=tkinter.W)

window.mainloop()
