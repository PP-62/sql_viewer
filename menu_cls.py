import tkinter as tk

from tkinter import messagebox

## make
#root = tk.Tk()
class Menu():
    def __init__(self,root,next_frame):

        self.data = {"host":None,"login":None,"password":None,"db":None}
        self.next_frame = next_frame
        
        self.menu = tk.Frame(root)
        front = tk.Label(self.menu, text = "Test")
        
        host_label = tk.Label(self.menu, text = "host:")
        self.host = tk.Entry(self.menu, width = 20)
        
        login_label = tk.Label(self.menu, text = "login:")
        self.login = tk.Entry(self.menu, width = 20)
        
        password_label = tk.Label(self.menu, text = "password:")
        self.password = tk.Entry(self.menu, width = 20)
        
        db_label = tk.Label(self.menu, text = "db:")
        self.db = tk.Entry(self.menu, width = 20)
        submit = tk.Button(self.menu,text = "continue",command = self.update)
## pack

        front.grid(row=0, column=0,columnspan = 2)
        host_label.grid(row=1, column=0)
        self.host.grid(row=1, column=1)

        login_label.grid(row=2, column=0)
        self.login.grid(row=2, column=1)

        password_label.grid(row=3, column=0)
        self.password.grid(row=3, column=1)

        db_label.grid(row=4, column=0)
        self.db.grid(row=4, column=1)

        submit.grid(row=5, column=0,columnspan = 2)

    def update(self):
        
        isgood = True
        self.data["host"] = self.host.get()
        self.data["login"] = self.login.get()
        self.data["password"] = self.password.get()
        self.data["db"] = self.db.get()
# проверить данные входа
        for i in self.data.values():
            if i == "":
                messagebox.showerror('Ошибка', ' Поля пустые.')
                isgood = False
                break
                
            if isgood:
                self.remove()
                self.next_frame.pack()
            
            else:
                messagebox.showerror("Ошибка", "Введены неправильные данные.")
            
    
    def pack(self):
        self.menu.pack()

    def remove(self):
        self.menu.pack_forget()
