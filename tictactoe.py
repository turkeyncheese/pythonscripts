import tkinter
from tkinter import *
import random

window = tkinter.Tk()
window.geometry('400x400')
window.resizable(0,0)
window.title('Rock, Paper, Scissors')
window.config(bg = 'grey')

tkinter.Label(window, text = 'Rock, Paper, Scissors', font = ('Arial', 20, 'bold'), bg = 'grey').pack()

tkinter.Label(window, text = 'Choose any one: Rock, Paper, Scissors', font = ('Arial', 15, 'bold'), bg = 'grey').place(x = 20, y = 70)
user_take = StringVar()

comp_pick = random.choice(['Rock', 'Paper', 'Scissors'])

Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Tie, you both selected ' + lowercase(user_pick) + '.')
    elif user_pick == 'Rock' and comp_pick == 'Paper':
        Result.set('You lose, computer selected paper.')
    elif user_pick == 'Rock' and comp_pick == 'Scissors':
        Result.set('You win, computer selected scissors.')
    elif user_pick == 'Paper' and comp_pick == 'Scissors':
        Result.set('You lose, computer selected scissors.')
    elif user_pick == 'Paper' and comp_pick == 'Rock':
        Result.set('You win, computer selected rock.')
    elif user_pick == 'Scissors' and comp_pick == 'Rock':
        Result.set('You lose, computer selected rock.')
    elif user_pick == 'Scissors' and comp_pick == 'Paper':
        Result.set('You win, computer selected paper.')
    else:
        Result.set('Invalid: Choose any one: Rock, Paper, Scissors')

def reset():
    Result.set('')
    user_take.set('')

def exit():
    window.destroy

tkinter.Entry(window, font = ('Arial', 10, 'bold'), textvariable = user_take, bg = 'white', width = 50,).place(x = 25, y = 110)

tkinter.Entry(window, font = ('Arial', 10, 'bold'), textvariable = Result, bg = 'white', width = 50,).place(x = 25, y = 250)

tkinter.Button(window, font = ('Arial', 13, 'bold'), text = 'PLAY', padx = 5, bg = 'grey', command = play).place(x = 150, y = 190)

tkinter.Button(window, font = ('Arial', 13, 'bold'), text = 'RESET', padx = 5,bg = 'grey', command = reset).place(x = 70,y = 310)

tkinter.Button(window, font = ('Arial', 13, 'bold'), text = 'EXIT', padx = 5, bg = 'grey', command = exit).place(x = 230,y = 310)

window.mainloop()
