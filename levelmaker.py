import tkinter
import const
from PIL import ImageTk, Image


def choose(sq, sq_u, sq_d, sq_l, sq_r):
    

def render():
    global panel, desk, painted
    
    for i in range(height):
        for j in range(width):
            if desk[i][j] == '#':
                panel.delete(painted[i][j])
                panel.create_image(j * const.BLOCK_SIZE + const.EPS_X, i * const.BLOCK_SIZE + const.EPS_Y)
            

def init():
    global root, name_panel, width_panel, height_panel, name, width, height
    
    root = None
    name_panel = None
    width_panel = None
    height_panel = None
    name = None
    width = None
    height = None


def sets():
    global name, width, height
    
    name = name_panel.get()
    width = int(width_panel.get())
    height = int(height_panel.get())
    
    root.destroy()
    

def get_settings():
    global root, name_panel, width_panel, height_panel
    
    root = tkinter.Tk()
    root.geometry(const.WINDOW_SIZE)
    root.title("Level maker 1.0")
        
    name_panel = tkinter.Entry()
    name_panel.insert(0, "Name...")
    name_panel.place(relx=0, rely=0, relwidth=1, relheight=0.25, anchor="nw")

    width_panel = tkinter.Entry()
    width_panel.insert(0, "Width...")
    width_panel.place(relx=0, rely=0.25, relwidth=1, relheight=0.25, anchor="nw")

    height_panel = tkinter.Entry()
    height_panel.insert(0, "Height...")
    height_panel.place(relx=0, rely=0.5, relwidth=1, relheight=0.25, anchor="nw")

    btn = tkinter.Button(text="Ok", command=sets)
    btn.place(relx=0.5, rely=0.75, relwidth=0.25, relheight=0.25, anchor="n")    
    
    root.mainloop()
    

def enter(event):
    global desk
    
    x_pos = event.x - const.EPS_X
    y_pos = event.y - const.EPS_Y
    
    if x_pos > width * const.BLOCK_SIZE or x_pos < 0:
        return
    
    if y_pos > height * const.BLOCK_SIZE or y_pos < 0:
        return
    
    
    x = x_pos // const.BLOCK_SIZE
    y = y_pos // const.BLOCK_SIZE
    
    if desk[y][x] == '#':
        return    
    
    desk[y][x] = '#'
    
    x_start = const.EPS_X + x * const.BLOCK_SIZE
    y_start = const.EPS_Y + y * const.BLOCK_SIZE
    
    painted[y][x] = panel.create_rectangle(x_start, y_start, x_start + const.BLOCK_SIZE, y_start + const.BLOCK_SIZE, fill="black")
    
    print(event.x, event.y)
    

if __name__ == '__main__':    
    init()
    #get_settings()
    
    name="a"
    width=10
    height=10
    
    root = tkinter.Tk()
    root.title("Editor 1.0 - " + name)
    root.geometry(const.get_size(width + 4, height))
    
    img1= Image.open("src/a.png")    
    img= ImageTk.PhotoImage(img1)
    
    print(const.BLOCK_SIZE)

    
    panel = tkinter.Canvas(width=const.BLOCK_SIZE * width + const.EPS_X, height=const.BLOCK_SIZE * height + const.EPS_Y)
    panel.place(relx=0, rely=0)
    
    panel.create_image(const.EPS_X, const.EPS_Y, image=img, anchor="nw")
    
    panel.create_line(const.BLOCK_SIZE * width - 1 + const.EPS_X, 0, const.BLOCK_SIZE * width - 1 + const.EPS_X, const.BLOCK_SIZE * height)
    
    btn_render = tkinter.Button(text="render")
    btn_render.place(relx=1, rely=0, height=const.BLOCK_SIZE, width=const.BLOCK_SIZE*4, anchor="ne")
    
    btn_save = tkinter.Button(text="save")
    btn_save.place(relx=1, rely=1/height, height=const.BLOCK_SIZE, width=const.BLOCK_SIZE*4, anchor="ne")    
    
    desk = [['.'] * width for i in range(height)]
    painted = [[None] * width for i in range(height)]    
    
    panel.bind('<1>', enter)
    root.mainloop()