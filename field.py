import tkinter
import threading

def load(number):
    fin = open('level'+str(number)+'.txt','r')
    field = fin.readlines()
    for i in range(len(field)):
        field[i] = field[i].strip()
    render = threading.Thread(target = field)
    render.start()

def field():
    global field
    game_window = tkinter.Tk()
    game_wiindow.title('GAME')
    game_window.geometry('600x600+300+300')
    
    game_field = tkinter.Canvas(game_window, width = 600, height = 600)
    game_field.place(relx=0, rely=0)
    
    root.protocol('WM_DELETE_WINDOW', game_window.destroy())
    
    const_len = 20
    for i in range(10, 601, const_len):
        for j in range(10, 601, const_len):
            if field[i][j] == '#':
                w.create_rectangle(j - const_len // 2, i + const_len // 2, j + const_len // 2, i - const_len // 2, fill = 'black')
            else:
                w.create_rectangle(j - const_len // 2, i + const_len // 2, j + const_len // 2, i - const_len // 2, fill = 'blue')
    game_window.mainloop()