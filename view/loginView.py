import json
import tkinter as tk
import webbrowser
import requests
from tkinter import messagebox 
from controller.LoginController import LoginController


class loginView:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.protocol('WM_DELETE_WINDOW', root.quit)
        self.root.geometry(f'400x360+500+100')
        self.root.resizable(False, False)
        self.root.iconbitmap(r'image\win.ico')


        def goLink(event):
                webbrowser.open_new('https://rofikit.com/registration')
        
        self.canvas = tk.Frame(self.root)
        self.canvas.pack(fill='both', anchor='center', padx=20, pady=20)
        
        frame = tk.Frame(self.canvas)
        frame.pack(side='top')
        
        title_frame = tk.Frame(frame)
        title_frame.pack(side='top')
        title_label = tk.Label(title_frame, text="Softwer Login", font=('Bahnschrift SemiBold Condensed', 18))
        title_label.pack(fill='both', pady=20)
        
        mobile_frame = tk.Frame(frame)
        mobile_frame.pack(side='top', pady=10)
        mobile_label = tk.Label(mobile_frame, text='Mobile No', width=12, font=('Bahnschrift SemiBold Condensed',13))
        mobile_label.pack(side='left', anchor='w')
        self.mobile_entry = tk.Entry(mobile_frame, width=25)
        self.mobile_entry.pack(side='left',ipady=2)
        
        password_frame = tk.Frame(frame)
        password_frame.pack(side='top', pady=10)
        password_label = tk.Label(password_frame, text='Password', width=12, font=('Bahnschrift SemiBold Condensed',13))
        password_label.pack(side='left', anchor='w')
        self.password_entry = tk.Entry(password_frame, show="*", width=25)
        self.password_entry.pack(side='left',ipady=2)
        
        button_frame = tk.Frame(frame)
        button_frame.pack(side='top', fill='both', anchor='center', pady=35)
        login_button = tk.Button(button_frame, text='Login', command=lambda:self.loginAction(), width=15, cursor="hand2", font=('Bahnschrift SemiBold Condensed', 10))
        login_button.pack(anchor='center')
        
        link_frame = tk.Frame(frame)
        link_frame.pack(side='top', fill='both', anchor='s', pady=20)
        link_label = tk.Label(link_frame, text='Create a new account', cursor="hand2", fg='#555')
        link_label.pack(side='bottom',anchor='s')
        link_label.bind("<Button-1>", goLink)

        self.mobile_entry.insert(0,"01737034338")
        self.password_entry.insert(0,"12115")

    def loginAction(self):
        mobile   = self.mobile_entry.get()
        password = self.password_entry.get()

        if mobile=='':
            messagebox.showwarning("Warning","Please enter a valid phone number")
        elif password=='':
             messagebox.showwarning("Warning","Please enter your secure password!")
        else:
            if self.checkConnection():
                self.root.destroy()
                LoginController(mobile,password)
            else:
                messagebox.showwarning("Connection Error","Chack your internet connection!")
            # self.root.destroy()
            # LoginController(mobile,password)


    def checkConnection(self):
        url = "http://www.google.com"
        timeout = 50
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.ConnectionError:
            return False
        except requests.Timeout:
            return False