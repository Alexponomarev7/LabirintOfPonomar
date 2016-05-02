import tkinter
#1368
def window_deleted():
    print(u'Окно закрыто, ёпть')
    root.destroy()

root = tkinter.Tk()
root.title(u"LabirintOfPonomar")
root.geometry('600x480+300+300')
root.protocol('WM_DELETE_WINDOW', window_deleted)
root.resizable(False, False)
root.mainloop()
