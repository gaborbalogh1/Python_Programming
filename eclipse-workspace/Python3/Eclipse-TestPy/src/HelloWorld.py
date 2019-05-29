'''
Created on 21 Oct 2018

@author: Gabor
'''
#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Hello World")
root.minsize(400, 400)

Label(root, text="Hello World from TKinter!").pack()

def msg():
    messagebox.showinfo("Gabor Says! ", "Hello from Message Box !")
    
Button(text= "Go", command= msg).pack()


root.mainloop()
