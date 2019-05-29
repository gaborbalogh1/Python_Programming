

import tkinter as tk
import tkinter.scrolledtext as scroll_txt

root = tk.Tk()
frame1 = tk.Frame(
    master=root,
    bg='#808000'
)
frame1.pack(fill='both', expand='yes')

editArea = scroll_txt.ScrolledText(
    master=root,
    wrap=tk.WORD,
    width=20,
    height=10
)
editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
editArea.insert(tk.INSERT,
"""\
Integer posuere erat a ante venenatis dapibus.
Posuere velit aliquet.
Aenean eu leo quam. Pellentesque ornare sem.
Lacinia quam venenatis vestibulum.
Nulla vitae elit libero, a pharetra augue.
Cum sociis natoque penatibus et magnis dis.
Parturient montes, nascetur ridiculus mus.
""")
root.mainloop()
