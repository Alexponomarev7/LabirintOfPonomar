import tkinter
from PIL import ImageTk, Image
import const
from choose import choose
from const import images, images_d1, render_levels
import threading
import time


def game(self):
    while True:
        self.x += self.dx
        self.y += self.dy
        
        if self.level[self.y][self.x] == '#':
            self.back(self)
        
        self.repaint()
                
        #time.sleep(1/8)

            

def render(self, i, j):
    if i < 0 or i >= self.height:
        return -1
    
    if j < 0 or j >= self.width:
        return -1
    
    if self.level[i][j] == '#':
        if i == 0:
            sq_u = True
        else:
            sq_u = (self.level[i - 1][j] != '#')
        
        
        if i == self.height - 1:
            sq_d = True
        else:
            sq_d = (self.level[i + 1][j] != '#')

                    
        if j == 0:
            sq_l = True
        else:
            sq_l = (self.level[i][j - 1] != '#')
                    
                    
        if j == self.width - 1:
            sq_r = True
        else:
            sq_r = (self.level[i][j + 1] != '#')
                
        img = choose(sq_u, sq_d, sq_l, sq_r)
        return images[img]
    else:
        return images[18]


class field:
    def __init__(self, root, back_img, h1, h2, level=1):
        self.h = [h1, h2]
        self.hnow = 0 
        self.dx = 0
        self.dy = 0
        
        self.root = root
        self.root.bind('<s>', self.try_down)
        self.root.bind('<w>', self.try_up)
        self.root.bind('<a>', self.try_left)
        self.root.bind('<d>', self.try_right)
                
        
        self.frame_field =  tkinter.Frame(root, width=580, height=460, bg='black', bd=5)
        self.frame_field.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)
                
        
        self.back_btn = tkinter.Label(self.frame_field, image=back_img, bg="black", cursor="hand2") 
        self.back_btn.place(anchor='ne', relx=1, rely=0)
        self.back_btn.bind('<1>', self.back) 
        
        f_r = open('./levels/lvl' + str(level) + ".txt", 'r')
        self.level = [[j for j in i.strip()] for i in f_r.read().split('\n')]
        f_r.close()
        
        self.width = len(self.level[0])
        self.height = len(self.level)

        
        self.desk_lab = [[None] * self.width for i in range(self.height)]
        
        for i in range(self.height):
            for j in range(self.width):
                if self.level[i][j] == "s":
                    self.x = j
                    self.y = i
        
        self.init()     
        
        threading.Thread(target=game, args=(self,)).start()
                    
        
    def back(self, event):
        self.frame_field.destroy()   

        
    def init(self):
        self.panel = tkinter.Canvas(self.frame_field, width=5+9* const.BLOCK_SIZE, height=5+9*const.BLOCK_SIZE, bd=0,bg="black")
        self.panel.place(x=0, y=0)
        self.pole = self.panel.create_image(5 + (4 - self.x) * 50, 5 + (4 - self.y)* 50, image=render_levels[1], anchor="nw")
        self.hero = self.panel.create_image(5 + 4 * 50, 5 + 4 * 50, image=self.h[0], anchor="nw")
        
        self.panel.focus_set()
        
    
    def repaint(self):
        dx = 10 * self.dx
        dy = 10 * self.dy
        
        last = time.time()
        
        self.panel.itemconfig(self.hero, image=self.h[self.hnow])
        self.hnow = (self.hnow + 1) % 2
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
                
                
    def try_up(self, event):
        if self.level[self.y - 1][self.x] != '#':
            self.dy = -1
            self.dx = 0
            
            
    def try_down(self, event):
        if self.level[self.y + 1][self.x] != '#':
            self.dy = 1
            self.dx = 0    
            
            
    def try_right(self, event):
        if self.level[self.y][self.x + 1] != '#':
            self.dy = 0
            self.dx = 1
            
    
    def try_left(self, event):
        if self.level[self.y][self.x - 1] != '#':
            self.dy = 0
            self.dx = -1  