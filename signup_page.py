import tkinter
import customtkinter
from PIL import ImageTk,Image
import hashlib
from tkinter import messagebox
import ast


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

signup_app = customtkinter.CTk()  #creating cutstom tkinter window
signup_app.geometry("600x440")
signup_app.title('Sign Up')


def signup_button_function():
    username_input = signup_username.get()
    password_input = signup_password.get()
    confirm_password_input = signup_cnf_password.get()
    
    
    if username_input is '' or password_input is '' or confirm_password_input is '':
        messagebox.showerror(title='Error',message="Fields can't be empty")
        return
    
    if check_var.get() == 0:
        messagebox.showerror(title='Error',message="You must agree to the terms and conditions")
        return

    if password_input==confirm_password_input:
        hashed_password = hashlib.sha256(password_input.encode()).hexdigest()
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            if username_input in r.keys():
                messagebox.showerror("Error", "Username already exists.")
                return

            dict2={username_input:hashed_password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))

            messagebox.showinfo("Success", "Account created successfully.")
            signup_app.destroy()    
            import main_menu_page  # switching to main menu page

        except:
            file=open('datasheet.txt','w')
            pp=str({'Username':'Password'})
            file.write(pp)
            file.close()
        
    else:
        messagebox.showerror('Invalid','Both Password should match')


def login_fun():
    signup_app.destroy()
    import login_page

img1=ImageTk.PhotoImage(Image.open("./images/doddle.png"))
l1=customtkinter.CTkLabel(master=signup_app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=330, height=420, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

signup_label =customtkinter.CTkLabel(master=frame, text="Create a new Account",font=('Century Gothic',22))
signup_label .place(x=40, y=45)

signup_username=customtkinter.CTkEntry(master=frame, width=230, placeholder_text='Username',font=('Arial',15))
signup_username.place(x=50, y=110)

signup_password=customtkinter.CTkEntry(master=frame, width=230, placeholder_text='Password', show="*",font=('Arial',15))
signup_password.place(x=50, y=160)

signup_cnf_password=customtkinter.CTkEntry(master=frame, width=230, placeholder_text='Confirm Password', show="*",font=('Arial',15))
signup_cnf_password.place(x=50, y=210)

check_var = customtkinter.IntVar(value=0)
checkbox = customtkinter.CTkCheckBox(master=frame, checkbox_height=15, checkbox_width=15, corner_radius=2, text="I agree to the Terms & Conditions", variable=check_var, onvalue=1, offvalue=0, font=('Arial',13))
checkbox.place(x=50,y=260)
#Create custom button
sign_up_btn = customtkinter.CTkButton(master=frame, width=230, text="Sign Up", command=signup_button_function, corner_radius=6)
sign_up_btn.place(x=50, y=300)


# l3 = customtkinter.CTkLabel(master=frame, text="- - - - - -  Or  - - - - - -", font=('Century Gothic', 16))
# l3.place(x=85, y=290)


l5=customtkinter.CTkLabel(master=frame, text="Already have an account.",font=('Century Gothic',12))
l5.place(x=45,y=347)

login_btn = customtkinter.CTkButton(master=frame,height=20 ,width=70, text="Login" , command= login_fun, corner_radius=6)
login_btn.place(x=212, y=350)


# You can easily integrate authentication system 

signup_app.mainloop()
