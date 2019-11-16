import tkinter as tk
from tkinter import Canvas
import os

class gui(tk.Frame):

    def __init__(self, width, height, title, master=None):
        self.width = width
        self.height = height
        self.title = title
        tk.Frame.__init__(self, master)
        self.master.title(self.title)
        self.master.wm_iconbitmap('turtle.ico')
        self.master.geometry(str(self.width) + 'x' + str(self.height + 25))
        self.master.resizable(0, 0)
        self.createCanvas()
        self.pack()

        def onClose():
            os._exit(0)

        self.master.protocol("WM_DELETE_WINDOW", onClose)

    def createCanvas(self):
        self.text = tk.Entry(self, width=self.width)
        self.text.pack()
        self.text.focus_set()
        self.canvas = Canvas(self.master, width=self.width, height=self.height, background='floral white')
        self.canvas.pack()
