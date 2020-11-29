import tkinter as tk
import winsound
from tkinter.scrolledtext import ScrolledText


def morse():
    morse_dict = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..',
                 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 
                 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                 '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-','\n':'-'}
    cipher = ''
    message = input_message.get('1.0',tk.END).upper()
    print(message)
    for letter in message:
        if letter != ' ':
            cipher += morse_dict[letter]+' '
        else:
            cipher += ' '
    cipher = cipher[:-2]
    output_message.insert(1.0, cipher)
    print(cipher)
    for ch in cipher:
        if ch == '.':
            winsound.Beep(1000,100)
        if ch == '-':
            winsound.Beep(1000,300)

root = tk.Tk()
root.title('Encrypt Message')
root.geometry('600x420+600+350')
root.resizable(False,False)
canvas = tk.Canvas(root,bg = '#DDCCBB',width = 600, height = 420).pack()
frame = tk.Frame(root, bg = '#FFEEDD').place(x=40,y=20,width=520,height=380)
input_message = ScrolledText(root, bd = 2, font = 'Ubuntu 12',bg = '#FFFEFD')
input_message.place(x=160,y=130,width=380,height=120)
output_message = ScrolledText(root, bd = 2, font = 'Ubuntu 12',bg = '#FFFEFD')
output_message.place(x=160,y=270,width=380,height=120)
tk.Label(root, text = 'Input Text',bg = '#DDCCBB', font = 'Ubuntu 14').place(x=40,y=170,width=120,height=40)
tk.Label(root, text = 'Output Text',bg = '#DDCCBB', font = 'Ubuntu 14').place(x=40,y=310,width=120,height=40)
tk.Button(root, text = 'Morse',bg = '#DDCCBB',font = 'Ubuntu 14',command = morse).place(x=440,y=30,width=100,height=30)

root.mainloop()