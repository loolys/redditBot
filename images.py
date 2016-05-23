import tkinter as tk
from PIL import Image, ImageTk
import time, os
import urllib.request
from io import BytesIO
from download import Reddit, Download


class Gui:
    def __init__(self):
    
        """ Download images and saves them into the folder images 
            shows them one by one in a tkinter window and then
            delete the folder after all images has been shown. """
    
        self.window = tk.Tk()
        pad = 3
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth()-pad, 
                    self.window.winfo_screenheight()-pad)) #Sets the window fullscreen
        self.label = tk.Label() 
        self.label.pack()            
        
        self.Reddit = Reddit()
        self.Download = Download()
        links = self.Reddit.reddit()
        for link in links:
            self.Download.download(link)
            
        files = os.listdir("images") # Creates an array with all filenames in images map

        
        counter = 0
        for file in files:
            if counter != 0 : time.sleep(10)
            photo = ImageTk.PhotoImage(Image.open("images/{}".format(file)))
            self.label.configure(image=photo)
            self.label.image = photo 
            self.window.update_idletasks()
            counter = 1
            
        self.Download.delete_folder()

      
if __name__ == "__main__":
    Gui()
    


