import random
import string
import tkinter as tk


def generate_block():
    chars = [random.choice(string.digits)]
    chars += [random.choice(string.ascii_uppercase) for _ in range(3)]
    random.shuffle(chars)  
    return ''.join(chars)


def generate_key():
    return '-'.join(generate_block() for _ in range(4))


def calc():
    entry_key.configure(state='normal') 
    entry_key.delete(0, tk.END)
    entry_key.insert(0, generate_key())
    entry_key.configure(state='readonly') 


window = tk.Tk()
window.title('Candy')
window.geometry('720x720')
window.resizable(False, False)

bg_img = tk.PhotoImage(file='bg_pic.png')
lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.8, anchor='center')

entry_key = tk.Entry(frame,
                     width=19,  
                     font=('Consolas', 18, 'bold'),
                     justify='center',
                     state='readonly')
entry_key.grid(column=0, row=0, padx=10, pady=15)

btn_calc = tk.Button(frame, text='Generate', command=calc)
btn_calc.grid(column=0, row=1, padx=10, pady=15)

window.mainloop()
