import tkinter as tk
from tkinter import *
import random 




class DND:

    def __init__(self):

#window
        
        self.window = tk.Tk()
        self.geo = self.window.geometry("500x500")
        self.title = self.window.title("Dice Roller")

        self.windowlabel = tk.Label(self.window, text="How many sides does the die have?",bg='PaleVioletRed1', font=('Arial', 10))
        self.windowlabel.place(relx = 0.5,
                                rely= 0.2, 
                                anchor= 'center' )



        self.window.configure(bg='PaleVioletRed1')
        self.entry = Entry(width=50)
        
        self.entry.place(relx = 0.5, rely= 0.3, anchor = 'center')
        self.btn = tk.Button(self.window,bg='PaleVioletRed4', text='Submit', font=('Arial', 10),command = self.roll)
        self.btn.place(relx = 0.5, rely = 0.5, anchor = 'center')
        


        self.window.mainloop()

    def roll(self):

        self.roll = random.choice(range(1,int(self.entry.get()) + 1))
        self.label = tk.Label(self.window, text = f'Roll: {self.roll}' )
        self.label.place(relx = 0.5, rely= 0.4, anchor = 'center')
        
#text
        



        

DND()