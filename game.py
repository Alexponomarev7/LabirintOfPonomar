import tkinter
import threading
import field

#1368
def window_deleted():
    print('Окно закрыто, ёпть')
    root.destroy()

root = tkinter.Tk()
root.title(u"LabirintOfPonomar")
root.geometry('600x480+300+300')
root.protocol('WM_DELETE_WINDOW', window_deleted)
root.resizable(False, False)
frame1 = tkinter.Frame(root, width = 580, height = 460, bg = 'black', bd = 5)
frame1.place(anchor = 'center', relx = 0.5, rely = 0.5, relwidth = 0.99, relheight = 0.99)
but1 = tkinter.Button(root, text = 'Начать игру', width = 25, height = 5, bg = 'white', fg = 'black', font = 'arial 14', command=field.load(1)) # вызов функции
but1.place(anchor = 'center', relx= 0.5, rely=0.3, relwidth = 0.25, relheight = 0.05)
levels = tkinter.Listbox(root, selectmode=tkinter.SINGLE)
lev = [u"Уровень 1", u"Уровень 2"]
for i in lev:
    levels.insert(tkinter.END, i)
levels.place(anchor = 'center', relx=0.5,  rely = 0.4, relwidth = 0.1, relheight = 0.1)
root.mainloop()
