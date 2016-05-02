import tkinter
import threading

def load(number=1):
    global fields
    
    fin = open('level'+str(number)+'.txt','r')
    fields = fin.readlines()
    for i in range(len(fields)):
        fields[i] = fields[i].strip()
    render = threading.Thread(target = field)
    render.start()

def field():
    global fields
    game_window = tkinter.Tk()
    game_window.title('GAME')
    game_window.geometry('600x600+300+300')
    
    game_field = tkinter.Canvas(game_window, width = 600, height = 600)
    game_field.place(relx=0, rely=0)
    
    game_window.protocol('WM_DELETE_WINDOW', game_window.destroy)
    
    const_len = 20
    for i in range(9, 390, const_len):
        for j in range(9, 390, const_len):
            if fields[(i - const_len // 2 + 1)//const_len][(j - const_len // 2 + 1)//const_len] == '#':
                game_field.create_rectangle(j - const_len // 2, i + const_len // 2, j + const_len // 2, i - const_len // 2, fill = 'black')
            else:
                game_field.create_rectangle(j - const_len // 2, i + const_len // 2, j + const_len // 2, i - const_len // 2, fill = 'blue')
    game_window.mainloop()