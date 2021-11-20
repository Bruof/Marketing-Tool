from tkinter import *
from tkinter import ttk

class EMVGUI:
    def __init__(self, top):

        self.top = top
        top.title('EMV Tool')

        frame = ttk.Frame(top, padding='3 3 12 12')
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        top.columnconfigure(0, weight=1)
        top.rowconfigure(0, weight=1)
        
        #Entry fields and creating variables
        self.units = DoubleVar()
        units_entry = ttk.Entry(frame, width=12, textvariable=self.units)
        units_entry.grid(column=1, row=2, sticky=(W, E))

        self.dolpe = DoubleVar()
        dolpe_entry = ttk.Entry(frame, width=12, textvariable=self.dolpe)
        dolpe_entry.grid(column=2, row=2, sticky=(W, E))

        self.prob = DoubleVar()
        prob_entry = ttk.Entry(frame, width=12, textvariable=self.prob)
        prob_entry.grid(column=3, row=2, sticky=(W, E))

        self.valEng = DoubleVar()
        valEng_entry = ttk.Entry(frame, width=12, textvariable=self.valEng)
        valEng_entry.grid(column=4, row=2, rowspan=3, sticky=(W, E))

        #Second set of Entry fields
        self.units2 = DoubleVar()
        units_entry = ttk.Entry(frame, width=12, textvariable=self.units2)
        units_entry.grid(column=1, row=3, sticky=(W, E))

        self.dolpe2 = DoubleVar()
        dolpe_entry = ttk.Entry(frame, width=12, textvariable=self.dolpe2)
        dolpe_entry.grid(column=2, row=3, sticky=(W, E))

        self.prob2 = DoubleVar()
        prob_entry = ttk.Entry(frame, width=12,  textvariable=self.prob2)
        prob_entry.grid(column=3, row=3, sticky=(W, E))


        #EMV output
        self.EMV = StringVar()
        ttk.Label(frame, textvariable=self.EMV).grid(column=5, row=2,  sticky=(W,E))

        #Calculate EMV Button
        ttk.Button(frame, text="Calculate EMV", command=self.calculateEMV).grid(column=6, row=2, sticky=W)

        #Labels
        ttk.Label(frame, text="Units").grid(column=1, row=1, sticky=(N, S))
        ttk.Label(frame, text="$ per each").grid(column=2, row=1, sticky=(N, S))
        ttk.Label(frame, text="Probability").grid(column=3, row=1, sticky=(N, S))
        ttk.Label(frame, text="Value Engineering").grid(column=4, row=1, sticky=(N, S))
        ttk.Label(frame, text="EMV").grid(column=5, row=1, sticky=(N, S))
        
        #Run the frame
        top.mainloop()

    def calculateEMV(self):
        units = self.units.get()
        units2 = self.units2.get()
        dolpe = self.dolpe.get()
        dolpe2 = (self.dolpe2.get())
        prob = (self.prob.get())
        prob2 = (self.prob2.get())
        result = ((units*dolpe)*prob)+((units2*dolpe2)*prob2)
        self.EMV.set(f'{round(result, 4):,}')
    pass