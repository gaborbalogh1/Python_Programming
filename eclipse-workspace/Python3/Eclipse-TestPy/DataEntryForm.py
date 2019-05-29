from tkinter import *
from tkinter import ttk

class DataEntry_Form:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "DATABASE ENTRY FORM")
        self.label.grid(row = 0, column = 0, columnspan = 2)
        
        ttk.Button(master, text = "ADD",
                   command = self.ADD_BTN).grid(row = 1, column = 0)

        ttk.Button(master, text = "REMOVE",
                   command = self.REMOVE_BTN).grid(row = 1, column = 1)

    def ADD_BTN(self):
        self.label.config(text = 'ADD STAFF TO DB')

    def REMOVE_BTN(self):
        self.label.config(text = 'REMOVED STAFF FROM DB')

            
def main():            
    
    root = Tk()
    app = DataEntry_Form(root)
    root.mainloop()
    
if __name__ == "__main__": main()