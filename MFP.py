from tkinter import *
from tkinter import ttk

class MFPGUI:
    def __init__(self, top):
        
        #Creating the Tkinter frame
        self.top = top
        top.title("MFP Tool")

        frm = ttk.Frame(top, padding="3 3 12 12")
        frm.grid(column=0, row=0, sticky=(N, W, E, S))
        top.columnconfigure(0, weight=1)
        top.rowconfigure(0, weight=1)

        #Last Year start
        self.productionLY = DoubleVar()
        productionLY_entry = ttk.Entry(frm, width=7, textvariable=self.productionLY)
        productionLY_entry.grid(column=2, row=1, sticky=(W, E))

        self.laborLY = DoubleVar()
        laborLY_entry = ttk.Entry(frm, width=7, textvariable=self.laborLY)
        laborLY_entry.grid(column=2, row=2, sticky=(W, E))

        self.laborLyCost = DoubleVar()
        laborLyCost_entry = ttk.Entry(frm, width=7, textvariable=self.laborLyCost)
        laborLyCost_entry.grid(column=2, row=3, sticky=(W, E))

        self.capitalInvestmentLY = DoubleVar()
        capitalInvestmentLY_entry = ttk.Entry(frm, width=7, textvariable=self.capitalInvestmentLY)
        capitalInvestmentLY_entry.grid(column=2, row=4, sticky=(W, E))

        self.capitalInvestmentCostsLY = DoubleVar()
        capitalInvestmentCostsLY_entry = ttk.Entry(frm, width=7, textvariable=self.capitalInvestmentCostsLY)
        capitalInvestmentCostsLY_entry.grid(column=2, row=5, sticky=(W, E))

        self.energyLY = DoubleVar()
        energyLY_entry = ttk.Entry(frm, width=7, textvariable=self.energyLY)
        energyLY_entry.grid(column=2, row=6, sticky=(W, E))

        self.energyCostsLY = DoubleVar()
        energyCosts_entry = ttk.Entry(frm, width=7, textvariable=self.energyCostsLY)
        energyCosts_entry.grid(column=2, row=7, sticky=(W, E))

        # This year start
        self.productionTY = DoubleVar()
        productionLY_entry = ttk.Entry(frm, width=7, textvariable=self.productionTY)
        productionLY_entry.grid(column=5, row=1, sticky=(W, E))

        self.laborTY = DoubleVar()
        laborLY_entry = ttk.Entry(frm, width=7, textvariable=self.laborTY)
        laborLY_entry.grid(column=5, row=2, sticky=(W, E))

        self.laborTYCost = DoubleVar()
        laborLyCost_entry = ttk.Entry(frm, width=7, textvariable=self.laborTYCost)
        laborLyCost_entry.grid(column=5, row=3, sticky=(W, E))

        self.capitalInvestmentTY = DoubleVar()
        capitalInvestmentLY_entry = ttk.Entry(frm, width=7, textvariable=self.capitalInvestmentTY)
        capitalInvestmentLY_entry.grid(column=5, row=4, sticky=(W, E))

        self.capitalInvestmentCostsTY = DoubleVar()
        capitalInvestmentCostsLY_entry = ttk.Entry(frm, width=7, textvariable=self.capitalInvestmentCostsTY)
        capitalInvestmentCostsLY_entry.grid(column=5, row=5, sticky=(W, E))

        self.energyTY = DoubleVar()
        energyLY_entry = ttk.Entry(frm, width=7, textvariable=self.energyTY)
        energyLY_entry.grid(column=5, row=6, sticky=(W, E))

        self.energyCostsTY = DoubleVar()
        energyCosts_entry = ttk.Entry(frm, width=7, textvariable=self.energyCostsTY)
        energyCosts_entry.grid(column=5, row=7, sticky=(W, E))

        #Results from Calculations
        self.MFPLY = StringVar()
        ttk.Label(frm, textvariable=self.MFPLY).grid(column=2, row=8, sticky=(W, E))

        self.MFPTY = StringVar()
        ttk.Label(frm, textvariable=self.MFPTY).grid(column=5, row=8, sticky=(W, E))

        self.PPC = StringVar()
        ttk.Label(frm, textvariable=self.PPC).grid(column=2, row=9, sticky=(W, E))

        #Multifactor Productivty Last Year Button
        ttk.Button(frm, text="Calculate", command=self.MFPLYCalculate).grid(column=4, row=8, sticky=W)

        #Multifactor Productivity This Year Button
        ttk.Button(frm, text="Calculate", command=self.MFPTYCalculate).grid(column=7, row=8, sticky=W)

        #Productivity Percent Change Button
        ttk.Button(frm, text="Calculate", command=self.productivityPercentChange).grid(column=4, row=9, sticky=W)

        #Last Year labels
        ttk.Label(frm, text="Production Last Year").grid(column=3, row=1, sticky=W)
        ttk.Label(frm, text="Labor Last Year").grid(column=3, row=2, sticky=W)
        ttk.Label(frm, text="Labor Costs Last Year").grid(column = 3, row=3, sticky=W)
        ttk.Label(frm, text="Capital Investments Last Year").grid(column=3, row=4, sticky=W)
        ttk.Label(frm, text="Captial Investment Costs Last Year").grid(column=3, row=5, sticky=W)
        ttk.Label(frm, text="Energy Used Last Year").grid(column=3, row=6, sticky=W)
        ttk.Label(frm, text="Energy Costs Last Year").grid(column=3, row=7, sticky=W)
        ttk.Label(frm, text="Multifactor Productivity for Last Year").grid(column=3, row=8, sticky=W)

        #This year labels
        ttk.Label(frm, text="Production This Year").grid(column=6, row=1, sticky=W)
        ttk.Label(frm, text="Labor This Year").grid(column=6, row=2, sticky=W)
        ttk.Label(frm, text="Labor Costs This Year").grid(column = 6, row=3, sticky=W)
        ttk.Label(frm, text="Capital Investments This Year").grid(column=6, row=4, sticky=W)
        ttk.Label(frm, text="Captial Investment Costs This Year").grid(column=6, row=5, sticky=W)
        ttk.Label(frm, text="Energy Used This Year").grid(column=6, row=6, sticky=W)
        ttk.Label(frm, text="Energy Costs This Year").grid(column=6, row=7, sticky=W)
        ttk.Label(frm, text="Multifactor Productivity for This Year").grid(column=6, row=8, sticky=W)

        #Productivity Percent Change Label
        ttk.Label(frm, text="Productivity Percent Change").grid(column=3, row=9, sticky=W)

        for child in frm.winfo_children():
            child.grid_configure(padx=5, pady=5)

        productionLY_entry.focus()

        top.mainloop()

    def MFPLYCalculate(self, *args) -> float:
        try:
            prodLY = float(self.productionLY.get())
            laborhrsLY = float(self.laborLY.get())
            laborcostsLY = float(self.laborLyCost.get())
            capInvLY = float(self.capitalInvestmentLY.get())
            capInvCostsLY = float(self.capitalInvestmentCostsLY.get())
            energyLY = float(self.energyLY.get())
            energyCostsLY = float(self.energyCostsLY.get())
            result = prodLY/((laborhrsLY*laborcostsLY)+(capInvLY*capInvCostsLY)+(energyLY*energyCostsLY))
            self.MFPLY.set(round(result, 4))
            return round(result, 4)
        except ValueError:
            pass
    
    def MFPTYCalculate(self, *args) -> float:
        try:
            prodTY = float(self.productionTY.get())
            laborhrsTY = float(self.laborTY.get())
            laborcostsTY = float(self.laborTYCost.get())
            capInvTY = float(self.capitalInvestmentTY.get())
            capInvCostsTY = float(self.capitalInvestmentCostsTY.get())
            energyTY = float(self.energyTY.get())
            energyCostsTy = float(self.energyCostsTY.get())
            result = prodTY/((laborhrsTY*laborcostsTY)+(capInvTY*capInvCostsTY)+(energyTY*energyCostsTy))
            self.MFPTY.set(round(result, 4))
            return round(result, 4)
        except ValueError:
            pass

    def productivityPercentChange(self, *args):
        try:
            MFPLY = self.MFPLYCalculate()
            MFPTY = self.MFPTYCalculate()
            result = ((MFPTY-MFPLY)/MFPLY)*100
            self.PPC.set(round(result, 5))
        except ValueError:
            pass