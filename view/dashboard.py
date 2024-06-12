import tkinter as tk
import webbrowser
from tkinter import messagebox 
from view import loginView

class Dashboard:
    def __init__(self,root):
        self.root = root
        self.root.title('User Dashboard')
        self.root.iconbitmap(r'image\mainwin.ico')
        self.root.protocol('WM_DELETE_WINDOW', root.quit)
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()-60
        self.root.geometry(f'{sw}x{sh}+{-10}+{0}')

        fram = tk.Frame(self.root)
        fram.pack(fill=tk.BOTH,side=tk.TOP)

        button = tk.Button(fram, text="Logout", command=self.logout, font=("Arial", 9))
        button.pack(side=tk.TOP,padx=30, pady=30, anchor='center')

    def logout(self):
        sms= messagebox.askquestion("Confirm","Are you sure to logout?") 
        if sms == "yes":
            self.root.destroy()
            loginView.loginView(tk.Tk())