# class for mob in LoP
class Mob:
    # init the mob
    def __init__(self):
        self.x = None
        self.y = None
        
        self.dx = 0
        self.dy = 0
    
    # trying change direction up
    def try_up(self, event):
        if self.level[self.y - 1][self.x] != '#':
            self.dy = -1
            self.dx = 0
            
    # trying change direction down        
    def try_down(self, event):
        if self.level[self.y + 1][self.x] != '#':
            self.dy = 1
            self.dx = 0    
            
    # trying change direction right
    def try_right(self, event):
        if self.level[self.y][self.x + 1] != '#':
            self.dy = 0
            self.dx = 1
            
    # trying change direction left
    def try_left(self, event):
        if self.level[self.y][self.x - 1] != '#':
            self.dy = 0
            self.dx = -1
            
    # making new animation
    def load_animation(self, images):
        self.animation = images
        self.current_image = self.animation[0]
        self.pos = 0
    
    # next frame animation
    def next_frame(self):
        self.pos = (self.pos + 1) % len(self.animation) 
        self.current_image = self.animation[self.pos]