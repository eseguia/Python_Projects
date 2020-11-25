import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import os

def write_file():
    with open((entry_path.get()+'.txt'), 'w+') as file:
        file.write(entry_text.get(1.0,tk.END))
def read_file():
    with open((entry_path.get()+'.txt'), 'r') as file:
        entry_text.delete(1.0,tk.END)
        text = file.read()
        entry_text.insert(1.0,text)
def delete_file():
    result = tk.messagebox.askyesno('DELETE','Do you wish to delete file?')
    if result == True:
        os.remove((entry_path.get()+'.txt'))
    else: pass
        
root = tk.Tk()
root.title('TXT file editor')
WIDTH, HEIGHT = 850,500
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()
frame = tk.Frame(root, bg = '#F5F79D')
frame.place(relwidth=1,relheight=1)

entry_path = tk.Entry(bd=3, relief='solid',font='Cambria 12')
entry_path.place(relx=0.3,rely=0.1,relwidth=0.65,relheight=0.1)
entry_text = ScrolledText(bd=3,relief='solid',font='Cambria 12')
entry_text.place(relx=0.3,rely=0.3,relwidth=0.65,relheight=0.6)
label1 = tk.Label(text='File Name',bg='#F0E888',font='Cambria 14').place(relx=0.05,rely=0.1,relwidth=0.2,relheight=0.1)
label2 = tk.Label(text='Text',bg='#F0E888',font='Cambria 14').place(relx=0.05,rely=0.3,relwidth=0.2,relheight=0.1)

button_write = tk.Button(root,text='Write',bg='#EEF142',bd=5,command=write_file)
button_write.place(relx=0.05,rely=0.45,relwidth=0.2,relheight=0.1)
button_read = tk.Button(root,text='Read',bg='#EEF142',bd=5,command=read_file)
button_read.place(relx=0.05,rely=0.6,relwidth=0.2,relheight=0.1)
button_delete = tk.Button(root,text='Delete',bd=5,bg='#EDB56F',command=delete_file)
button_delete.place(relx=0.05,rely=0.8,relwidth=0.2,relheight=0.1)

root.mainloop()
