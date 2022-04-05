# Text Widget
# Tx = Text(root, bg, fg, bd, height, width, font, ..)

from tkinter import *

win = Tk()
win.geometry("300x300")
win.title("Simple Question Answer")

def textInput():
    Input = inputxt.get("1.0","end-1c")
    print(Input)
    if(Input =="625"):
        Output.insert(END, 'Your answer is correct')
    else:
        Output.insert(END, 'Incorrect answer')

inputxt = Text(win, height=10, width=30, bg = "light cyan")
l = Label(text="What is 25X25 ?")

Output =Text(win,height=10, width=30, bg='light yellow')

btn = Button(win, height=2, width=15, text="Result", command= lambda:textInput())

l.pack()
inputxt.pack()
Output.pack()
btn.pack()

mainloop()