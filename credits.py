import tkinter
from PIL import ImageTk, Image

# class which contains credits
class Credits:
    def __init__(self, root, loader=None):
        self.frame = tkinter.Frame(root, width=580, height=460, bg='black', bd=5)
        self.loader = loader
        
        back_img = self.loader.load("back.png", size=(110, 40))
        credits_img = self.loader.load("credits_info.png")
        
        self.back_btn = tkinter.Label(self.frame, image=back_img, bg="black", cursor="hand2") 
        self.back_btn.place(anchor='ne', relx=1, rely=0)
        
        tkinter.Label(self.frame, image=credits_img, bg="black").place(relx=0.5, rely=0.5, anchor="center")
        self.back_btn.bind('<1>', self.destroy)
        
    # destroying this frame
    def destroy(self, event):
        self.frame.place_forget() 
        
    # placing this frame
    def create(self, event):
        self.frame.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)