from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Feedback Form")
root.resizable(False, False)
frame = ttk.Frame(root)
frame.config(height=100, width=200)
frame.pack()

frame2 = ttk.Frame(root)
frame.config(height=100, width=200)
frame2.pack()


def callback():
    messagebox.showinfo(title='Feedback Form Submit!', message='Feedback submitted!')
    print('clicked')


def clear():
    entry_name.delete(0, 'end')
    entry_email.delete(0, 'end')
    text_comments.delete(1.0, 'end')
    messagebox.showinfo(title='Form was reset', message='data was cleared!')
    print('cleared text in name, email, comments.')


button = ttk.Button(frame2, text="Submit", width=10, command=callback).grid(row=4, column=0)

button2 = ttk.Button(frame2, text="Clear Text!", width=10, command=clear).grid(row=4, column=1)

logo = PhotoImage(file='tour_logo.gif')

label1 = ttk.Label(frame, image=logo).grid(row=0, column=0, rowspan=2)
label2 = ttk.Label(frame, text='Thanks for taking part in our session,'
                               'Please leave your comments below:', wraplength=280).grid(row=1, column=1)

label_name = ttk.Label(frame2, text='Name: ', font=('Ariel', 14)).grid(row=0, column=0, padx=5, sticky='sw')
label_email = ttk.Label(frame2, text='Email: ', font=('Ariel', 14)).grid(row=0, column=1, padx=5, sticky='sw')
label_comments = ttk.Label(frame2, text='Comments: ', font=('Ariel', 10)).grid(row=2, column=0, padx=5, sticky='sw')

entry_name = ttk.Entry(frame2, width=23, font=('Arial', 10))
entry_email = ttk.Entry(frame2, width=23, font=('Arial', 10))
text_comments = Text(frame2, width=50, height=20, font=('Arial', 10))

entry_name.grid(row=1, column=0, padx=5, sticky='w')
entry_email.grid(row=1, column=1, padx=5, sticky='w')
text_comments.grid(row=3, column=0, columnspan=2, padx=5,)


root.mainloop()
