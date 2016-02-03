# -*- coding: utf-8 -*-
### Author: Daniël Vercouteren


import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import datetime
import DatabaseNieuw

#BARCHART
def createBarchart():
    plt.xlabel('Sentiment')
    plt.ylabel('Aantal')
    plt.title('ISCP - Daniël Vercouteren: Bar Chart')

    #X is negatief, neutraal, positief
    #Y is het aantal
    data = ['Negatief', 'Neutraal', 'Positief']
    x = np.arange(len(data))
    y = DatabaseNieuw.getAnalysis()
    width = 0.8

    plt.bar(x, y, width, color = "darkblue")
    plt.xticks(x + 0.4, data)

    plt.tight_layout()
    plt.show()

#TIMECHART
def createTimechart():
    plt.figure(figsize=(30,10))
    tijdLijst = []
    scoreLijst = []

    data = DatabaseNieuw.getTimeChart()
    for rij in data:
        tijdLijst.append(datetime.datetime.fromtimestamp(rij[0]/1000.0))
        scoreLijst.append(rij[1])

    plt.plot(tijdLijst, scoreLijst)
    plt.show()

#PIECHART
def createPiechart():
    plt.title('ISCP - Daniël Vercouteren: Pie Chart')

    dataLabels = "Negatief", "Neutraal", "Positief"
    dataSize = DatabaseNieuw.getAnalysis()
    colors = "firebrick", "darkorange", "forestgreen"
    explode = (0, 0, 0)

    plt.pie(dataSize, explode=explode, labels=dataLabels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')

    plt.show()

def panel():
    window = tk.Tk()
    window.title("ISCP opdracht Daniël Vercouteren")
    window.resizable(width=False, height=False)
    window.minsize(width=400, height=100)

    Button1 = tk.Button(window, text="Open de bar chart!", command = lambda: createBarchart(), bg = "darkblue", fg="white", font="Helvetica")
    Button1.config(height=5, width=25, bd=4)
    Button2 = tk.Button(window, text="Open de tijdlijn!", command = lambda: createTimechart(), bg = "darkblue", fg="white", font="Helvetica")
    Button2.config(height=5, width=25, bd=4)
    Button3 = tk.Button(window, text="Open de pie chart!", command = lambda: createPiechart(), bg = "darkblue", fg="white", font="Helvetica")
    Button3.config(height=5, width=25, bd=4)

    Button1.pack()
    Button2.pack()
    Button3.pack()

    window.mainloop()