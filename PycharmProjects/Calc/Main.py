from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Python Calculator')
root.resizable(False, False)
root.geometry('360x145+300+300')

# Frame to set the view
frame = ttk.Frame(root, width='370', height='370')
frame.pack()

# Style the buttons
style = ttk.Style()
style.configure('TButton', foreground='orange')

# Calculator will need a grid of 6X4
label = Label(frame, width=40, height=1, background="grey")
label.grid(row=0, column=0, columnspan=6)

# the clear button


def clear():
    label['text'] = '0'


def click():
    print('clicked button')


def get_button_click():
    print("clicked ")


# Number Buttons First

button1 = ttk.Button(frame, text='1', command=lambda: get_button_click(1)).grid(row=5, column=0)
button2 = ttk.Button(frame, text='2', command=lambda: get_button_click(2)).grid(row=5, column=1)
button3 = ttk.Button(frame, text='3', command=lambda: get_button_click(3)).grid(row=5, column=2)

button4 = ttk.Button(frame, text='4', command=lambda: get_button_click(4)).grid(row=4, column=0)
button5 = ttk.Button(frame, text='5', command=lambda: get_button_click(5)).grid(row=4, column=1)
button6 = ttk.Button(frame, text='6', command=lambda: get_button_click(6)).grid(row=4, column=2)
button7 = ttk.Button(frame, text='7', command=lambda: get_button_click(7)).grid(row=3, column=0)
button8 = ttk.Button(frame, text='8', command=lambda: get_button_click(8)).grid(row=3, column=1)
button9 = ttk.Button(frame, text='9', command=lambda: get_button_click(9)).grid(row=3, column=2)

button0 = ttk.Button(frame, text='0', command=lambda: get_button_click(0)).grid(row=6, column=0, columnspan=2)

# Functions Buttons Second
button10 = ttk.Button(frame, text="+", command=click).grid(row=5, column=3)
button11 = ttk.Button(frame, text="-", command=click).grid(row=4, column=3)
button12 = ttk.Button(frame, text="/", command=click).grid(row=1, column=3)
button13 = ttk.Button(frame, text="%", command=click).grid(row=1, column=2)
button14 = ttk.Button(frame, text="*", command=click).grid(row=3, column=3)
button14 = ttk.Button(frame, text="=", command=click).grid(row=6, column=3)
button15 = ttk.Button(frame, text='.', command=click).grid(row=6, column=2)
button16 = ttk.Button(frame, text='AC', command=clear).grid(row=1, column=0)
button17 = ttk.Button(frame, text='+/-', command=click).grid(row=1, column=1)


root.mainloop()
