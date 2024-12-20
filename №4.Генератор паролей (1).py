from tkinter import *
from random import choice


def randomize():
    lengthPassword = e.get()
    e.delete (0, END)
    for i in range(int(lengthPassword)):
        e.insert(0, choice(alphabet))


root = Tk()
root.title('Генератор паролей')
root.geometry('500x200')
#root.resizble(width=False, height=False)

alphabet = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
e = Entry(root, font='Arial 13')
e.place(relx=0.5, y=20, anchor=CENTER)

btn = Button(root, text='Сгенерировать', font=('Times New Roman', 17, 'bold'), command=randomize)
btn.place(relx=0.5, y=75, anchor=CENTER)



root.mainloop()
