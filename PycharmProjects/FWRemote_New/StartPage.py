import tkinter as tk
from tkinter import *
from tkinter import ttk, PhotoImage, messagebox as msg, scrolledtext as sct


win1 = tk.Tk()
win1.title('MATW FWRemote')
win1.resizable(0, 0)
win1.minsize(width='520', height='600')
win1.config(bg='#C0C0C0')
win1.iconbitmap('FWRemoteR.icns')

image = "sMtw.png"
photo = PhotoImage(file=image).subsample(6, 6)

st = ttk.Style(win1)
st.theme_use('default')
st.configure('TLabel', foreground='white', background='red')


def mouse_enter(event):
    global prev
    target_IP.delete(0, END)
    prev = event


def exit_btn():
    win1.quit()
    win1.destroy()
    exit()


def submit():
    msg.askquestion('MSG Box', message='MATW FW Remote MSG box'+'\n\nDo you like the app so far?', parent=win1)
    print('Submit Button clicked...')  # for testing only remove this line before packaging


lbl1 = ttk.Label(win1, image=photo).grid(column='0', row='0', columnspan='4', rowspan='1', padx=5, pady=5,
                                         sticky='ns')
lbl2 = ttk.Label(win1, text='Target IP', width='15', style='TLabel').grid(column='1', row='4', padx=5, pady=5,
                                                                          sticky='nsew')

lbl3 = ttk.Label(win1, text='Enter User Name', width='15').grid(column='1', row='5', padx=5, pady=5, sticky='nsew')

lbl4 = ttk.Label(win1, text='Enter Password', width='15').grid(column='1', row='6', padx=5, pady=5, sticky='nsew')

lbl5 = ttk.Label(win1, text='Local Only', width='15').grid(column='3', row='3', padx=5, pady=5, sticky='nsew')
lbl6 = ttk.Label(win1, text='Admin Free', width='15').grid(column='3', row='5', padx=5, pady=5, sticky='nsew')
lbl7 = ttk.Label(win1, text='Show Log Viewer', width='15').grid(column='3', row='6', padx=5, pady=5, sticky='nsew')
lbl8 = ttk.Label(win1, text='Select One or More File Sets', width='15').grid(column='2', row='7',
                                                                             padx=5, pady=5, sticky='nsew')

browser = ttk.Button(win1, text='Client Browser', width='15').grid(column='2', row='3', padx=5)
get_status = ttk.Button(win1, text='Get Status', width='15').grid(column='3', row='4', padx=5)
exit_btn = ttk.Button(win1, text='Exit', width='15', command=exit_btn).grid(column='2', row='11', padx=10, pady=10)

v = tk.StringVar()
v.set("Enter_Target_IP_or_localhost")  # setting the Entry widget text to default

v2 = tk.StringVar()
v2.set("Enter_User_Name")  # setting the Entry widget text to default

v3 = tk.StringVar()
v3.set("Enter_Password")  # setting the Entry widget text to default


target_IP = ttk.Entry(win1, textvariable=v).grid(column='2', row='4', padx=5)
username = ttk.Entry(win1, textvariable=v2).grid(column='2', row='5', padx=5)
pass_word = ttk.Entry(win1, textvariable=v3, show='*').grid(column='2', row='6', padx=5)
text_Select_option = sct.ScrolledText(win1, width=50, height=10, wrap=tk.WORD)
text_Select_option.grid(column='1', row='8', columnspan='8')
submit_btn = ttk.Button(command=submit, text='Submit').grid(column=1, row=11)

chk_bx1 = ttk.Checkbutton(win1).grid(column='4', row=3)
chk_bx2 = ttk.Checkbutton(win1).grid(column='4', row=5)
chk_bx3 = ttk.Checkbutton(win1).grid(column='4', row=6)


def display_list():
    f = 'Display_List'
    text_Select_option.insert(END, open(f).read())
    text_Select_option['font'] = ('Arial', '16')


display_list()


win1.mainloop()
