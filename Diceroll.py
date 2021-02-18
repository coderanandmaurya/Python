#Step 1: Importing the required modules
import  tkinter
import random

#Step 2: Building a top-level widget to make the main window for our application
root =tkinter.Tk()
root.geometry('250x250')
root.title('Musketeer_Dice')

label=tkinter.Label(root,font=("times",200))

#Step 3: Designing the buttons
def roll():
    number=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685",]
    label.config(text=f"{random.choice(number)}")
    label.pack()

button = tkinter.Button(root, text='Shake',  command=roll)
button.pack()

root.mainloop()