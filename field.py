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
        back_img = self.loader.load("back.png", size=(110, 40))
        
        self.back_btn = tkinter.Label(self.frame, image=back_img, bg="black", cursor="hand2") 
        self.back_btn.place(anchor='ne', relx=1, rely=0)
        self.back_btn.bind('<1>', self.destroy) 
        
    # creating the frame
    def create(self, event):
        self.level_number = 1  
        self.hero = Mob()                
        
        self.root.bind('<s>', self.hero.try_down)
        self.root.bind('<w>', self.hero.try_up)
        self.root.bind('<a>', self.hero.try_left)
        self.root.bind('<d>', self.hero.try_right)
        
        self.frame.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)   
        self.panel = tkinter.Canvas(self.frame, width=const.WIDTH_PANEL, height=const.HEIGHT_PANEL, bd=0, bg="black")
        self.panel.place(x=0, y=0)
        
        threading.Thread(target=self.play).start()
    
    # playing process
    def play(self):
        self.alive = True
        
        animation = [self.loader.load("man1.png", size=(50, 50)),
                     self.loader.load("man2.png", size=(50, 50))]
        self.hero.load_animation(animation)        
        
        self.load_level(self.level_number)
                
        self.map_img = render_map(self, self.level_number, self.loader)
        
        self.map_image = ImageTk.PhotoImage(self.map_img)
        
        x = 5 + (4 - self.hero.x) * 50
        y = 5 + (4 - self.hero.y) * 50
        
        self.pole = self.panel.create_image(x, y, image=self.map_image, anchor="nw")
        self.hero_img = self.panel.create_image(5 + 4 * 50, 5 + 4 * 50, image=self.hero.current_image, anchor="nw")
        
        while self.alive:
            self.hero.x += self.hero.dx
            self.hero.y += self.hero.dy
        
            if self.level[self.hero.y][self.hero.x] == '#':
                self.gameover = self.loader.load("gameover.gif")
                self.panel.create_image(5 + 25 + 4 * 50, 5 + 25 + 4 * 50, image=self.gameover, anchor="center")
                
                time.sleep(0.5)
                self.destroy(0)
                return
                    
            self.repaint()
            
            if self.level[self.hero.y][self.hero.x] == 'f':
                self.hero.dx = 0
                self.hero.dy = 0
                self.alive = False
        
        self.nextlevel = self.loader.load("next_level.gif")
        lol = self.panel.create_image(5 + 25 + 4 * 50, 5 + 25 + 4 * 50, image=self.nextlevel, anchor="center")
        time.sleep(1)
        self.panel.delete(lol)
        
        self.level_number += 1
        self.load_level(self.level_number)
        self.play()
        
    
    # destroy the frame    
    def destroy(self, event):
        self.frame.unbind('<s>')
        self.frame.unbind('<w>')
        self.frame.unbind('<a>')
        self.frame.unbind('<d>')
        
        self.alive = False
        
        self.frame.place_forget()   

    # repaint function
    def repaint(self):
        dx = 10 * self.hero.dx
        dy = 10 * self.hero.dy
        
        """new_map = self.map_img 
        for i in range(-4, 5):
            for j in range(-4, 5):
                length = max(abs(i), abs(j))
                if not (self.hero.x + i >= 0 and self.hero.x+ i < self.width):
                    continue
                
                if not (self.hero.y + j >= 0 and self.hero.y + j < self.height):
                    continue
                
                for x in range(50):
                    for y in range(50):
                        px = new_map.getpixel(((self.hero.x + i) * 50 + x, (self.hero.y + j) * 50 + y))
                        new_map.putpixel(((self.hero.x + i) * 50 + x, (self.hero.y + j) * 50 + y), (px[0] - length * 10, px[1] - length * 10, px[2] - length * 10))
                        
        self.new_map = ImageTk.PhotoImage(new_map)"""
        
        last = time.time()
        
        self.hero.next_frame()
        self.panel.itemconfig(self.hero_img, image=self.hero.current_image)
        
        for i in range(5):
            self.panel.move(self.pole, -dx, -dy)   
            #self.panel.itemconfig(self.pole, image=self.new_map)            
            while time.time() - last < (i + 1) * (0.2) / 5:
                continue
            
    
    def load_level(self, level=1):        
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