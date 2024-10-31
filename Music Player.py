import os
import pygame
import tkinter as tk
from tkinter import filedialog


class Music():
    
    def __init__(self):
        
        pygame.mixer.init()
        
        #main window
        
        self.music_window = tk.Tk()
        self.music_window.title('Music Player')
        self.music_window.geometry('800x500')
        self.song_label = tk.Label(self.music_window, text="No song loaded", relief="sunken")
        self.song_label.place(relx= 0.5, rely= 0.4, anchor = 'center')
        
        #load button
        self.load_button = tk.Button(self.music_window, text= "Load", command= self.load_music)
        self.load_button.place(relx=0.06, rely=0.05, anchor= "center")
        
        #play button
        self.unpause_button = tk.Button(self.music_window, text= "     ▶️", width = 2, command= self.unpause_music)
        self.unpause_button.place(relx=0.45, rely=0.51, anchor= "center")
        
        #pause button
        self.play_button = tk.Button(self.music_window, text= "⏸️", width= 2, command= self.pause_music)
        self.play_button.place(relx=0.55, rely=0.51, anchor= "center")
        

        #restart button
        self.restart_button = tk.Button(self.music_window, text= "🔄", width= 2, command= self.restart_music)
        self.restart_button.place(relx=0.6, rely=0.6, anchor= "center")
        
        #volume scale
        self.volume_scale = tk.Scale(self.music_window, from_= 0, to_=1, orient= "vertical", resolution= 0.05, command= self.volume_slider)
        self.volume_scale.set(0.5)
        self.volume_scale.place(relx= 0.65, rely= 0.53, anchor='center')
        
        
        self.music_window.mainloop()
        
        
    def load_music(self):
        self.file = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3;*.wav")])
        if self.file: #checks for validity // returns a boolean i think T or F, meaning if its valid, the loop goes.
            pygame.mixer.music.load(self.file)
            pygame.mixer.music.play()  
            self.song_label.config(text=f"Now Playing: {os.path.basename(self.file)}")
    
    def unpause_music(self):
        pygame.mixer.music.unpause()
    
    
    def pause_music(self):
        pygame.mixer.music.pause()
        
            
    def restart_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()  
            pygame.mixer.music.load(self.file)  
            pygame.mixer.music.play() 
            
    def volume_slider(self,value):
        pygame.mixer.music.set_volume(float(value))
            

    
    
    

        
        


Music()


