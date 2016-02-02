import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import datetime
import DatabaseNieuw

#BARCHART
def createBarchart():
    #X is negatief, neutraal, positief
    #Y is het aantal
    data = ['Negatief', 'Neutraal', 'Positief']
    x = np.arange(len(data))
    y = DatabaseNieuw.getAnalysis()
    width = 0.8

    plt.bar(x, y, width, color = "yellow")
    plt.xticks(x + 0.4, data)

    plt.tight_layout()
    plt.show()

def createTimechart():
    tijdLijst = []
    scoreLijst = []

    data = DatabaseNieuw.getTimeChart()
    for rij in data:
        tijdLijst.append(datetime.datetime.fromtimestamp(rij[0]/1000.0))
        scoreLijst.append(rij[1])

    plt.plot(tijdLijst, scoreLijst)
    plt.show()


def panel():
    window = tk.Tk()
    window.title("ISCP opdracht Daniël Vercouteren")

    Button1 = tk.Button(window, text="Open de bar chart!", command = lambda: createBarchart())
    Button2 = tk.Button(window, text="Open de tijdlijn!", command = lambda: createTimechart())

    Button1.pack()
    Button2.pack()

    window.mainloop()

panel()