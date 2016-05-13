from PIL import ImageTk, Image
import field
import const
from choose import choose

class render_data:
    def __init__(self, level, width, height):
        self.level = level
        self.width = width
        self.height = height         


def render_map(self, level, ld):
    f_r = open('./levels/lvl' + str(level) + ".txt", 'r')
    level = [[j for j in i.strip()] for i in f_r.read().split('\n')]
    f_r.close()
    
    width = len(level[0])
    height = len(level)    
    
    maps = Image.new("RGBA", (width * 50, height * 50))
    for i in range(height):
        for j in range(width):
            maps.paste(render(render_data(level, width, height), i, j), (j * 50, i * 50))
            
    self.buffer.append(maps)
    
    return self.buffer[-1]
    

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
            return const.images[img]
        else:
            return const.images[18]