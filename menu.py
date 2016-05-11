import tkinter
import const

# class which contains menu items
class Menu:
    # init the frame Menu
    def __init__(self, root, loader=None):
        self.frame = tkinter.Frame(root, width=const.WIDTH_FRAME, height=const.HEIGHT_FRAME, bg='black', bd=5)
        self.loader = loader
        
        tower_img = self.loader.load("tower.png")
        tkinter.Label(self.frame, image=tower_img, bg="black").place(anchor="center", relx=0.15, rely=0.4) 
        tkinter.Label(self.frame, image=tower_img, bg="black").place(anchor="center", relx=0.85, rely=0.4) 
        
        credits_img = self.loader.load("credits.png", size=(200, 40))
        new_game_img = self.loader.load("new game.png", size=(200, 40))
        levels_img = self.loader.load("levels.png", size=(200, 40))
        
        self.new_game_btn = tkinter.Label(self.frame, image=new_game_img, bg="black", cursor="hand2") 
        self.new_game_btn.place(anchor='center', relx=0.5, rely=0.3)
                
        self.levels_btn = tkinter.Label(self.frame, image=levels_img, bg="black", cursor="hand2") 
        self.levels_btn.place(anchor='center', relx=0.5, rely=0.4)
            
        self.credits_btn = tkinter.Label(self.frame, image=credits_img, bg="black", cursor="heart") 
        self.credits_btn.place(anchor='center', relx=0.5, rely=0.5)
    
    # place this frame on root Tk
    def create(self):
        self.frame.place(anchor="center", relx=0.5, rely=0.5, relwidth=1, relheight=1)