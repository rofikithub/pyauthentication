import tkinter as tk
from view.loginView import loginView


class App:
    def __init__(self, root):
        loginView(root)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()