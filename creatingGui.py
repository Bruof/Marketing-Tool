from tkinter import *
from tkinter import ttk

from MFP import MFPGUI


class CreateHomeGUI:
    
    def __init__(self):
        top = Tk()
        top.title('Marketing Tool Home')
        
        frame = ttk.Frame(top, padding="3 3 12 12")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        top.columnconfigure(0, weight=1)
        top.rowconfigure(0, weight=1)

        ttk.Button(frame, text='Multifactor Productivity', command=MFPGUI).grid(column=1, row=1, sticky=(W, E))

        top.mainloop()

CreateHomeGUI()