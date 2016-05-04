import tkinter
import threading
import field
import credits
from PIL import ImageTk, Image
from const import images, images_d1, render_levels

def credits_open(event):    
    credits.create_credits(root, back_img, credits_info_img)
    
    
def field_open(event):    
    field.field(root, back_img, hero0, hero1)


def load():
    for i in range(7):
        if i > 1:
            for j in range(4):
                
                img = Image.open("src/sprite_" + str(i + 1) + ".png").resize((50, 50))
                images.append(img.rotate(90 * j))
              #  images_d1.append(ImageTk.PhotoImage(Image.eval(img, func).rotate(90 * j)))
        else:
            img = Image.open("src/sprite_" + str(i + 1) + ".png").resize((50, 50))
            images.append(img)
          #  images_d1.append(ImageTk.PhotoImage(Image.eval(img, func)))
 
 
class render_data:
    def __init__(self, level, width, height):
        self.level = level
        self.width = width
        self.height = height
          
            
def render_map(level):
    f_r = open('./levels/lvl' + str(level) + ".txt", 'r')
    level = [[j for j in i.strip()] for i in f_r.read().split('\n')]
    f_r.close()
    
    width = len(level[0])
    height = len(level)    
    
    maps = Image.new("RGBA", (width * 50, height * 50))
    for i in range(height):
        for j in range(width):
            maps.paste(field.render(render_data(level, width, height), i, j), (j * 50, i * 50))
            
    render_levels.append(ImageTk.PhotoImage(maps))
    #self.maps.save("map1.png", "PNG")


if __name__ == '__main__':
    root = tkinter.Tk()
    
    load()
    root.title(u"Labirint Of Ponomar")
    root.geometry('600x480+300+300')
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    root.resizable(False, False)
    
    
    render_map(1)
    
    hero0 = ImageTk.PhotoImage(Image.open("src/man1.png").resize((50, 50))) 
    hero1 = ImageTk.PhotoImage(Image.open("src/man2.png").resize((50, 50))) 
    
    frame_menu = tkinter.Frame(root, width = 580, height = 460, bg = 'black', bd = 5)
    frame_menu.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)
    
    back_img = ImageTk.PhotoImage(Image.open("src/back.png").resize((110, 40)))    
    credits_info_img = ImageTk.PhotoImage(Image.open("src/credits_info.png"))    
    
    new_game_img = ImageTk.PhotoImage(Image.open("src/new game.png").resize((200, 40)))
    new_game_btn = tkinter.Label(frame_menu, image=new_game_img, bg="black", cursor="hand2") 
    new_game_btn.place(anchor = 'center', relx=0.5, rely=0.3)
    new_game_btn.bind('<1>', field_open)
        
    levels_img = ImageTk.PhotoImage(Image.open("src/levels.png").resize((200, 40)))
    levels_btn = tkinter.Label(frame_menu, image=levels_img, bg="black", cursor="hand2") 
    levels_btn.place(anchor = 'center', relx=0.5, rely=0.4)
    
    credits_img = ImageTk.PhotoImage(Image.open("src/credits.png").resize((200, 40)))
    credits_btn = tkinter.Label(frame_menu, image=credits_img, bg="black", cursor="heart") 
    credits_btn.place(anchor = 'center', relx=0.5, rely=0.5)    
    credits_btn.bind('<1>', credits_open)
    
    tower_img = ImageTk.PhotoImage(Image.open("src/tower.png"))
    tkinter.Label(frame_menu, image=tower_img, bg="black").place(anchor = 'center', relx=0.15, rely=0.4) 
    tkinter.Label(frame_menu, image=tower_img, bg="black").place(anchor = 'center', relx=0.85, rely=0.4) 
            
    root.mainloop()
