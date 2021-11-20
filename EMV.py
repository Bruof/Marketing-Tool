from tkinter import *
from tkinter import ttk

class EMVGUI:
    def __init__(self):

        top = Tk()
        top.title('EMV Tool')

        frame = ttk.Frame(top, padding='3 3 12 12')
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        top.columnconfigure(0, weight=1)
        top.rowconfigure(0, weight=1)
        
        #Entry fields and creating variables
        self.units = StringVar()
        units_entry = ttk.Entry(frame, width=12, textvariable=self.units)
        units_entry.grid(column=1, row=2, sticky=(W, E))

        self.dolpe = StringVar()
        dolpe_entry = ttk.Entry(frame, width=12, textvariable=self.dolpe)
        dolpe_entry.grid(column=2, row=2, sticky=(W, E))

        self.prob = StringVar()
        prob_entry = ttk.Entry(frame, width=12, textvariable=self.prob)
        prob_entry.grid(column=3, row=2, sticky=(W, E))

        self.valEng = StringVar()
        valEng_entry = ttk.Entry(frame, width=12, textvariable=self.valEng)
        valEng_entry.grid(column=4, row=2, rowspan=3, sticky=(W, E))

        #Second set of Entry fields
        self.units2 = StringVar()
        units_entry = ttk.Entry(frame, width=12, textvariable=self.units2)
        units_entry.grid(column=1, row=3, sticky=(W, E))

        self.dolpe2 = StringVar()
        dolpe_entry = ttk.Entry(frame, width=12, textvariable=self.dolpe2)
        dolpe_entry.grid(column=2, row=3, sticky=(W, E))

        self.prob2 = StringVar()
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
        
        #Run the fram
        top.mainloop()

    def calculateEMV(self, *args):
        units = float(self.units.get())
        units2 = float(self.units2.get())
        dolpe = float(self.dolpe.get())
        dolpe2 = float(self.dolpe2.get())
        prob = float(self.prob.get())
        prob2 = float(self.prob2.get())
        result = ((units*dolpe)*prob)+((units2*dolpe2)*prob2)
        self.EMV.set(f'{round(result, 4):,}')
    pass

EMVGUI()