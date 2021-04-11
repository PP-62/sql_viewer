## main
from menu_cls import *
from main_cls import *
from grid_func import *
import tkinter as tk

root = tk.Tk()
main_frame = Main(root)
menu = Menu(root,main_frame)
menu.pack()
##
##df = test_DF()
##table = table_from_DF(root,df)
##table.pack(expand=tk.YES, fill=tk.BOTH)
 
