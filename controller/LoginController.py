import json
import tkinter as tk
import requests
from view.messageView import messageView
from tkinter import messagebox 

class LoginController:
    def __init__(self,mobile,password):
        self.mobile = mobile
        self.password = password
        self.userLogin()

    def login(self):
        with open("user.json", 'r') as f:
            data = json.load(f)
            messageView(tk.Tk(),data)



    def userLogin(self):
        data = {
            "mobile": self.mobile,
            "password": self.password
        }

        #link = 'http://127.0.0.1:8000/softwer/login/'+ str(self.mobile) + '/' + str(self.password)
        link = 'https://rofikit.com/softwer/login/'+ str(self.mobile) + '/' + str(self.password)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "*",
            "Connection": "keep-alive",
            'Content-Type': 'application/json',
        }
        res = requests.get(link, headers=headers, data={'mobile':"01322852974",'password':"12345678"})
        data = (res.json())
        #print(data)
        #messagebox.showerror("error","Invalid your mobile or password!")
        messageView(tk.Tk(),data)




