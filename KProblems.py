from tkinter import *
from tkinter import ttk
from typing import Sized

class KProblemsGUI:

    def __init__(self) -> None:
        #Create the tkinter window
        top = Tk()
        top.title("KProblems Tool")
        top.columnconfigure(0, weight=1)
        top.rowconfigure(0, weight=1)

        #Create the frame inside the TK window
        frame = ttk.Frame(top, padding="3 3 12 12")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))

        #Create the K1 Entry Fields
        self.k1prod1 = DoubleVar()
        kprod1_entry = ttk.Entry(frame, width=10, textvariable=self.k1prod1)
        kprod1_entry.grid(column=2, row=2, sticky=(W, E))

        self.k1numdays1 = DoubleVar()
        knumdays1_entry = ttk.Entry(frame, width=10, textvariable=self.k1numdays1)
        knumdays1_entry.grid(column=3, row=2, sticky=(W, E))

        self.k1costs1 = DoubleVar()
        kcosts1_entry = ttk.Entry(frame, width=10, textvariable=self.k1costs1)
        kcosts1_entry.grid(column=4, row=2, sticky=(W, E))

        self.k1sellp1 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k1sellp1)
        ksellp1_entry.grid(column=5, row=2, sticky=(W, E))

        self.k1dcosts1 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k1dcosts1)
        ksellp1_entry.grid(column=6, row=2, sticky=(W, E))

        self.k1prob1 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k1prob1)
        ksellp1_entry.grid(column=7, row=2, sticky=(W, E))

        self.k1ndefect1 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k1ndefect1)
        ksellp1_entry.grid(column=8, row=2, sticky=(W, E))

        #Second set for K1
        self.k1prod2 = DoubleVar()
        kprod1_entry = ttk.Entry(frame, width=10, textvariable=self.k1prod2)
        kprod1_entry.grid(column=2, row=3, sticky=(W, E))

        self.k1numdays2 = DoubleVar()
        knumdays1_entry = ttk.Entry(frame, width=10, textvariable=self.k1numdays2)
        knumdays1_entry.grid(column=3, row=3, sticky=(W, E))

        self.k1costs2 = DoubleVar()
        kcosts1_entry = ttk.Entry(frame, width=10, textvariable=self.k1costs2)
        kcosts1_entry.grid(column=4, row=3, sticky=(W, E))

        self.k1sellp2 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k1sellp2)
        ksellp1_entry.grid(column=5, row=3, sticky=(W, E))

        self.k1dcosts2 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k1dcosts2)
        ksellp1_entry.grid(column=6, row=3, sticky=(W, E))

        self.k1prob2 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k1prob2)
        ksellp1_entry.grid(column=7, row=3, sticky=(W, E))

        self.k1ndefect2 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k1ndefect2)
        ksellp1_entry.grid(column=8, row=3, sticky=(W, E))

        #Spacer between K1 and K2
        ttk.Separator(frame, orient='horizontal').grid(column=2, row=4, rowspan=1, columnspan=11, sticky=(E, W))

        #Create the K2 Entry Fields
        self.k2prod1 = DoubleVar()
        kprod1_entry = ttk.Entry(frame, width=10, textvariable=self.k2prod1)
        kprod1_entry.grid(column=2, row=5, sticky=(W, E))

        self.k2numdays1 = DoubleVar()
        knumdays1_entry = ttk.Entry(frame, width=10, textvariable=self.k2numdays1)
        knumdays1_entry.grid(column=3, row=5, sticky=(W, E))

        self.k2costs1 = DoubleVar()
        kcosts1_entry = ttk.Entry(frame, width=10, textvariable=self.k2costs1)
        kcosts1_entry.grid(column=4, row=5, sticky=(W, E))

        self.k2sellp1 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k2sellp1)
        ksellp1_entry.grid(column=5, row=5, sticky=(W, E))

        self.k2dcosts1 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k2dcosts1)
        ksellp1_entry.grid(column=6, row=5, sticky=(W, E))

        self.k2prob1 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k2prob1)
        ksellp1_entry.grid(column=7, row=5, sticky=(W, E))

        self.k2ndefect1 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k2ndefect1)
        ksellp1_entry.grid(column=8, row=5, sticky=(W, E))

        #Second set for K2
        self.k2prod2 = DoubleVar()
        kprod1_entry = ttk.Entry(frame, width=10, textvariable=self.k2prod2)
        kprod1_entry.grid(column=2, row=6, sticky=(W, E))

        self.k2numdays2 = DoubleVar()
        knumdays1_entry = ttk.Entry(frame, width=10, textvariable=self.k2numdays2)
        knumdays1_entry.grid(column=3, row=6, sticky=(W, E))

        self.k2costs2 = DoubleVar()
        kcosts1_entry = ttk.Entry(frame, width=10, textvariable=self.k2costs2)
        kcosts1_entry.grid(column=4, row=6, sticky=(W, E))

        self.k2sellp2 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k2sellp2)
        ksellp1_entry.grid(column=5, row=6, sticky=(W, E))

        self.k2dcosts2 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k2dcosts2)
        ksellp1_entry.grid(column=6, row=6, sticky=(W, E))

        self.k2prob2 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k2prob2)
        ksellp1_entry.grid(column=7, row=6, sticky=(W, E))

        self.k2ndefect2 = DoubleVar()
        ksellp1_entry = ttk.Entry(frame, width=10, textvariable=self.k2ndefect2)
        ksellp1_entry.grid(column=8, row=6, sticky=(W, E))

        #Separator between K2 and K3
        ttk.Separator(frame, orient='horizontal').grid(column=2, row=8, rowspan=1, columnspan=11, sticky=(E, W))


        #Labels to determine which one is K1 - K3
        ttk.Label(frame, text="K1").grid(column=1, row=2, sticky=(N, S))
        ttk.Label(frame, text="K2").grid(column=1, row=5, sticky=(N, S))

        #Create the Labels for the Data entries
        ttk.Label(frame, text="Daily Production").grid(column=2, row=1, sticky=(N, S))
        ttk.Label(frame, text="Number of Days").grid(column=3, row=1, sticky=(N, S))
        ttk.Label(frame, text="Unit Costs").grid(column=4, row=1, sticky=(N, S))
        ttk.Label(frame, text="Sell Price").grid(column=5, row=1, sticky=(N, S))
        ttk.Label(frame, text="Design Costs").grid(column=6, row=1, sticky=(N, S))
        ttk.Label(frame, text="Probability of Occurence").grid(column=7, row=1, sticky=(N, S))
        ttk.Label(frame, text="Non-Defective Rate").grid(column=8, row=1, sticky=(N, S))
        ttk.Label(frame, text="Sales of Non-Defects").grid(column=9, row=1, sticky=(N, S))
        ttk.Label(frame, text="Costs").grid(column=10, row=1, sticky=(N, S))
        ttk.Label(frame, text="Expected Profit").grid(column=11, row=1, sticky=(N, S))
        ttk.Label(frame, text="EMV").grid(column=12, row=1, sticky=(N, S))

        top.mainloop()
        pass

KProblemsGUI()