import tkinter
from tkinter import ttk


def reset():
    selected.set("")


def miOption():
    print("Has seleccionado: ", selected.get())


window = tkinter.Tk()
selected = tkinter.StringVar()
selected.set("")

r1 = ttk.Radiobutton(window, text='Si', value='Si', variable=selected, command=miOption)
r1.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)
r2 = ttk.Radiobutton(window, text='No', value='No', variable=selected, command=miOption)
r2.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)
r3 = ttk.Radiobutton(window, text='Quizás', value='Quizás', variable=selected, command=miOption)
r3.grid(column=0, row=2, sticky=tkinter.W, pady=5, padx=5)
button_reset = tkinter.Button(window, text='Reset', command=reset)
button_reset.grid(column=2, row=4, sticky=tkinter.E, pady=5, padx=5)
option_label = ttk.Label(window, textvariable=selected)
option_label.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()
