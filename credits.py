import tkinter
from PIL import ImageTk, Image


def back(event):
    frame_credits.place_forget()   


def create_credits(root, back_img, credits_img):
    global frame_credits    
    
    frame_credits = tkinter.Frame(root, width=580, height=460, bg='black', bd=5)
    
    back_btn = tkinter.Label(frame_credits, image=back_img, bg="black", cursor="hand2") 
    back_btn.place(anchor='ne', relx=1, rely=0)
    
    tkinter.Label(frame_credits, image=credits_img, bg="black").place(relx=0.5, rely=0.5, anchor="center")
    
    frame_credits.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)

    back_btn.bind('<1>', back)    


frame_credits = None 