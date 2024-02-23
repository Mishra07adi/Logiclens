import tkinter
import customtkinter
from PIL import ImageTk,Image
from tkinter import messagebox


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green



w = customtkinter.CTk()  
w.geometry("1280x720")
w.title('Welcome')
img123=ImageTk.PhotoImage(Image.open("./images/doddle.png"))
l123=customtkinter.CTkLabel(master=w,image=img123)
l123.pack()
l1=customtkinter.CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)

w.mainloop()
