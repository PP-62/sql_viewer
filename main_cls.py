import tkinter as tk
from grid_func import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Main():
    def __init__(self,root):
        self.data = pd.DataFrame(data={})
        self.main = tk.Frame(root)
        
        self.table_frame = tk.Frame(self.main)
        self.table = table_from_DF(self.table_frame,self.data)
        
        self.graph_frame = tk.Frame(self.main)
        self.current_type = "pie"
        self.graph_type = tk.Button(self.graph_frame,text = "type",command = self.change_graph)


        self.command_frame = tk.Frame(self.main)
        self.command = tk.Entry(self.command_frame, width = 20)
        execute_button = tk.Button(self.command_frame,text = "execute",command = self.execute)

        self.graph_type.pack(side="right")
        self.table_frame.pack(side="top")
        self.table.pack()
        self.graph_frame.pack(side="top")
        
        self.command_frame.pack(side="top")
        self.command.pack(side="left")
        execute_button.pack(side="left")


    def change_graph(self):
        
        ### нариовать граф
        pass

    def execute(self):
        
        ### выполнить комманду
        pass

    def pack(self):
        self.main.pack()

    def remove(self):
        self.main.pack_forget()
