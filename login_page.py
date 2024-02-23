import tkinter
import customtkinter
from PIL import ImageTk,Image
import hashlib
from tkinter import messagebox
import ast

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark 
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


def login_button_function():
    username_input = username.get()
    password_input = hashlib.sha256(password.get().encode()).hexdigest()

    if username_input is '' or password_input is '':
        messagebox.showerror(title='Error',message="Fields can't be empty")
        return

    file=open('datasheet.txt','r')
    data=file.read()
    r=ast.literal_eval(data)
    file.close()

    if username_input in r.keys() and password_input==r[username_input]:
        login_app.destroy()            # destroy current window and creating new one 
        import main_menu_page
    else:
        messagebox.showerror("Authentication Failed", "Invalid username or password.")


def signup_fun():
    login_app.destroy()
    import signup_page


login_app = customtkinter.CTk()  #creating cutstom tkinter window
login_app.geometry("600x440")
login_app.title('Login')


img1=ImageTk.PhotoImage(Image.open("./images/doddle.png"))
l1=customtkinter.CTkLabel(master=login_app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=330, height=380, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',22))
l2.place(x=50, y=45)

username=customtkinter.CTkEntry(master=frame, width=230, placeholder_text='Username',font=('Arial',15))
username.place(x=50, y=110)

password=customtkinter.CTkEntry(master=frame, width=230, placeholder_text='Password', show="*",font=('Arial',15))
password.place(x=50, y=165)

# l3=customtkinter.CTkLabel(master=frame, text="Forget password?",font=('Century Gothic',12))
# l3.place(x=155,y=195)

#Create custom button
login_btn1 = customtkinter.CTkButton(master=frame, width=230, text="Login", command=login_button_function, corner_radius=6)
login_btn1.place(x=50, y=240)


# l4 = customtkinter.CTkLabel(master=frame, text="- - - - - -  OR  - - - - - -", font=('Century Gothic', 16))
# l4.place(x=85, y=270)

l5=customtkinter.CTkLabel(master=frame, text="Don't have an account?",font=('Century Gothic',12.5))
l5.place(x=45,y=300)

signup_btn1 = customtkinter.CTkButton(master=frame,height=20 ,width=80, text="Sign Up", command=signup_fun, corner_radius=6)
signup_btn1.place(x=210, y=303)


login_app.mainloop()
