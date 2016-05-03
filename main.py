#!/usr/bin/python
from tkinter import *
import random
root = Tk()
canv = Canvas(root, width=640, height=480)
canv.pack()
canv.create_rectangle(0, 0, 640, 480, fill="white")
root.resizable(0, 0)
COUNT=150
elements=[]
for i in range(0, COUNT):
  elements.append(canv.create_oval(320 - 8, 240 - 8, 320 + 8, 240 + 8, fill="green"))
def tick():
  rem = 10
  for i in elements:
    canv.move(i, random.randrange(-4, 4), random.randrange(-4, 4))
    rem -= 1
    if rem <= 0: break
  root.after(40, tick)
tick()
root.mainloop()