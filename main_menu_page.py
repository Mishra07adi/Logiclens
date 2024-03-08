import tkinter
import customtkinter
from PIL import ImageTk,Image
from tkinter import messagebox


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


win_mainmenu = customtkinter.CTk()  
# win_mainmenu.geometry("1280x720+0+0")
win_mainmenu.after(0, lambda:win_mainmenu.state('zoomed'))
win_mainmenu.title('System Management Dashboard')
win_mainmenu.iconbitmap('images/logo.ico')
# img123=ImageTk.PhotoImage(Image.open("./images/doddle.png"))
# wallpaper=customtkinter.CTkLabel(master=win_mainmenu)
# wallpaper.pack()


#creating custom frame
# top_frame=customtkinter.CTkFrame(master=wallpaper, width=1180, height=620, corner_radius=15)
# frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# heading1=customtkinter.CTkLabel(master=win_mainmenu, text="Welcome to Logiclens",font=('Century Gothic',60))
# heading1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)

# frame_1 = customtkinter.CTkFrame(master=win_mainmenu,fg_color='#aaaaaa')
# frame_1.pack(pady=2.5)

# frame_2 = customtkinter.CTkFrame(master=win_mainmenu,fg_color='#f3f6f4')
# frame_2.pack(pady=2.5)

# frame_3 = customtkinter.CTkFrame(master=win_mainmenu,fg_color='#dadada')
# frame_3.pack(pady=2.5)

# frame_4 = customtkinter.CTkFrame(master=win_mainmenu,fg_color='#dadada')
# frame_4.pack(pady=2.5)

main_frame = customtkinter.CTkFrame(master=win_mainmenu,fg_color='#011f4b')
main_frame.pack(fill="both",expand=True)

top_frame = customtkinter.CTkFrame(master=main_frame,fg_color='#6497b1')
top_frame.pack(padx=3,pady=3,fill='x',expand=False)
# top_frame.pack(padx=3,pady=3,fill="both",expand=True,rely=0.3)

bottom_frame = customtkinter.CTkFrame(master=main_frame,fg_color='#6497b1')
bottom_frame.pack(padx=3,pady=3,fill='both',expand=True)






win_mainmenu.mainloop()
