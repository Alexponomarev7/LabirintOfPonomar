import tkinter
import threading
import const
    
from field import Field
from credits import Credits
from menu import Menu
from loader import Loader

from PIL import ImageTk, Image


if __name__ == '__main__':
    # init main window
    root = tkinter.Tk()
        
    # window customization
    root.title(const.TITLE)
    root.geometry(const.WINDOW_SIZE)
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    root.resizable(False, False)
    
    # creating Loader object
    ld = Loader()
    
    # loading base blocks
    for i in range(const.BLOCK_COUNT):
        const.blocks.append(ld.load("sprite_" + str(i + 1) + ".png", tk=False, size=(50, 50)))
        
    # making frame menu object
    frame_menu = Menu(root, loader=ld)
    
    # making frame field object
    frame_field = Field(root, loader=ld)    
    
    # making frame credits object
    frame_credits = Credits(root, loader=ld)
    
    # configurate menu object
    frame_menu.new_game_btn.bind('<1>', frame_field.create)
    frame_menu.credits_btn.bind('<1>', frame_credits.create)
    
    # loading level 1
    frame_field.load_level()
    
    # placing menu object
    frame_menu.create()    
    
    # main looping
    root.mainloop()