import tkinter
import time
import const
import threading

from mob import Mob
from render import render_map

from PIL import ImageTk, Image
                

class Field:
    def __init__(self, root, loader=None):                
        self.frame = tkinter.Frame(root, width=const.WIDTH_FRAME, height=const.HEIGHT_FRAME, bg='black', bd=5)
        self.loader = loader
        self.buffer = []
        self.root = root
        
        self.hero = Mob()        
        animation = [self.loader.load("man1.png", size=(50, 50)),
                     self.loader.load("man2.png", size=(50, 50))]
        self.hero.load_animation(animation)
        
        back_img = self.loader.load("back.png", size=(110, 40))
        
        self.back_btn = tkinter.Label(self.frame, image=back_img, bg="black", cursor="hand2") 
        self.back_btn.place(anchor='ne', relx=1, rely=0)
        self.back_btn.bind('<1>', self.destroy) 
        
    
    def create(self, event):
        self.root.bind('<s>', self.hero.try_down)
        self.root.bind('<w>', self.hero.try_up)
        self.root.bind('<a>', self.hero.try_left)
        self.root.bind('<d>', self.hero.try_right)
        
        self.frame.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)   
        self.panel = tkinter.Canvas(self.frame, width=const.WIDTH_PANEL, height=const.HEIGHT_PANEL, bd=0, bg="black")
        self.panel.place(x=0, y=0)
        threading.Thread(target=self.play).start()
        self.alive = True
    
    
    def play(self):
        map_image = render_map(self, self.level, self.loader)
        self.map_image = ImageTk.PhotoImage(map_image)
        
        x = 5 + (4 - self.hero.x) * 50
        y = 5 + (4 - self.hero.y) * 50
        
        self.pole = self.panel.create_image(x, y, image=self.map_image, anchor="nw")
        self.hero_img = self.panel.create_image(5 + 4 * 50, 5 + 4 * 50, image=self.hero.current_image, anchor="nw")
        
        while self.alive:
            self.hero.x += self.hero.dx
            self.hero.y += self.hero.dy
        
            if self.level[self.hero.y][self.hero.x] == '#':
                self.back(self)
                return
        
            self.repaint()
    
        
    def destroy(self, event):
        self.frame.unbind('<s>')
        self.frame.unbind('<w>')
        self.frame.unbind('<a>')
        self.frame.unbind('<d>')
        
        self.alive = False
        
        self.frame.place_forget()   

            
    def repaint(self):
        dx = 10 * self.hero.dx
        dy = 10 * self.hero.dy
        
        last = time.time()
        
        self.hero.next_frame()
        self.panel.itemconfig(self.hero_img, image=self.hero.current_image)
        
        self.panel.move(self.pole, -dx, -dy)            
        while time.time() - last < (0.2) / 5:
            continue
        
        self.panel.move(self.pole, -dx, -dy)            
        while time.time() - last < 2 * (0.2) / 5:
            continue

        self.panel.move(self.pole, -dx, -dy)            
        while time.time() - last < 3 * (0.2) / 5:
            continue

        self.panel.move(self.pole, -dx, -dy)            
        while time.time() - last < 4 * (0.2) / 5:
            continue

        self.panel.move(self.pole, -dx, -dy)            
        while time.time() - last < 5 * (0.2) / 5:
            continue
    
    
    
    def load_level(self, level=1):
        self.level_number = level
        
        f_r = open('./levels/lvl' + str(level) + ".txt", 'r')
        self.level = [[j for j in i.strip()] for i in f_r.read().split('\n')]
        f_r.close()
        
        self.width = len(self.level[0])
        self.height = len(self.level)        
        
        for i in range(self.height):
            for j in range(self.width):
                if self.level[i][j] == "s":
                    self.hero.y = i
                    self.hero.x = j
                    
        self.hero.level = self.level