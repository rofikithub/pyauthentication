import math
import tkinter as tk
from datetime import date, datetime, timedelta
import webbrowser
from datetime import date
from view.dashboard import Dashboard
from view import loginView


class messageView:
    def __init__(self,root,data):
        self.root = root
        self.root.title('Notification')
        self.root.protocol('WM_DELETE_WINDOW', root.quit)
        self.root.geometry(f'400x300+500+100')
        self.root.resizable(False, False)
        self.root.iconbitmap(r'image\email.ico')
        
        self.version = "1.0.2"

        def updateVersion(event):
            webbrowser.open_new('https://rofikit.com/')
            self.root.destroy()
            loginView.loginView(tk.Tk())


        # Data ///////
        

        fram = tk.Frame(self.root)
        fram.pack(side='top', fill='both')

        sms_label = tk.Label(fram, text='Hello\n'+str(data["user"])+'\n Welcome to '+str(data["name"]), fg='#555', font=("Bahnschrift SemiBold Condensed", 12))
        sms_label.pack(side='top', fill='x', padx=20, pady=40, anchor='w')

        if self.version != data["version"]:
            link_label = tk.Label(fram, text='New version '+str(data["version"])+' is available, Click for Download', fg='#555', cursor="hand2", font=("Bahnschrift SemiBold Condensed", 10))
            link_label.pack(side='top', anchor='center')
            link_label.bind("<Button-1>", updateVersion)

        
        link_label = tk.Label(fram, text='The package will expire on '+str(data["end"]), fg='#777', font=('Bahnschrift SemiBold Condensed', 9))
        link_label.pack(side='top', anchor='center')

        e = date.fromisoformat(data["end"])
        end = datetime(e.year, e.month, e.day)
        end = end.timestamp()
        end = math.ceil(end)

        today = datetime.today()
        today = today.timestamp()
        today = math.ceil(today)

        if today > end :
            sms_label.configure(text='Hi,\n'+str(data["name"])+'\n This package has expired at '+str(data["end"]))
            #print ("Package has expired!")
            button = tk.Button(fram, text="Renew", command=self.packageRenew, width=15, cursor="hand2", font=('Arial', 10))
            button.pack(side='top', fill='none', padx=10, pady=40, anchor='s')
        else:
            button = tk.Button(fram, text="Dashboard", command=self.nextAction, width=15, cursor="hand2", font=('Arial', 10))
            button.pack(side='top', fill='none', padx=10, pady=40, anchor='s')


    def packageRenew(self):
        webbrowser.open_new('https://rofikit.com/')
        self.root.destroy()
        loginView.loginView(tk.Tk())

    def nextAction(self):
        self.root.destroy()
        Dashboard(tk.Tk())

