from tkinter import *

from random import *

clicks = 0

def randomize():

   global clicks

   btnClick.place(x=randint(70, 1000), y=randint(70, 650))

   clicks += 1

   labelClick['text'] = str(clicks)

   labelClick.pack()

root = Tk()

root.title('Клікер')

root.geometry('1280x720')

root.resizable(width=False, height=False)

root['bg'] = 'yellow'

labelClick = Label(root, text='0', font=('Comic Sans MS', 30, 'bold'), bg='yellow', fg='black')

labelClick.pack()

btnClick = Button(root,

                 text='Click me!',

                 bg='blue',

                 fg='black',

                 padx='20',

                 pady='8',

                 font=('Comic Sans MS', 13, 'bold'),

                 command=randomize

                 )

btnClick.place(x=randint(70, 1000), y=randint(70, 650))

root.mainloop()