import matplotlib.pyplot as plt
import numpy as np
from Aufgabe5 import f


def bisektion_iterationen(funktion: str, a: float, b: float, epsilon: float = 0.000001) -> list:
    """Führt das Bisektionsverfahren aus und speichert alle Iterationen

    Args:
        funktion (str): Funktion als string
        a (float): 1. Intervallsgrenze
        b (float): 2. Intervallsgrenze
        epsilon (float, optional): Genauigkeit

    Returns:
        list: Liste mit allen Iterationen (a, b, c, fc)
    """

    iterationen = []

    while True:
        c = (a + b) / 2
        fc = f(c, funktion)

        #speichert aktuelles Intervall und Näherung der Nullstelle
        iterationen.append((a, b, c, fc))

        #Abbruchbedingung
        if abs(fc) <= epsilon:
            break

        #Intervall wird halbiert (Vorzeichenwechsel prüfen)
        if f(a, funktion) * fc < 0:
            b = c
        else:
            a = c

    return iterationen
    

def plotter(iterationen: list, funktion: str, a: float, b: float) -> None:
    """Visualisieren der Iterationen des Bisektionsverfahrens

    Args:
        iterationen (list): Liste mit allen Iterationen (a, b, c, fc)
        funktion (str): Funktion als string
        a (float): 1. Intervallsgrenze
        b (float): 2. Intervallsgrenze
    """


    lösung = []
    genauigkeit = []

    #Erzeugt x-Werte für den Funktionsgraphen
    x = np.linspace(a, b, 500)
    y = [f(xi, funktion) for xi in x]

    plt.ion()

    for a, b, c, fc in iterationen:
        lösung.append(c)
        genauigkeit.append(abs(fc))

        plt.clf()

        #Diagramm 1: Funktion und Intervall
        plt.subplot(2, 1, 1)
        plt.plot(x,y)
        plt.axhline(0, color='red', linestyle='--')
        plt.axvline(c, color='green', linestyle='--')
        plt.axvline(a, color='blue', linestyle='--')
        plt.axvline(b, color='orange', linestyle='--')
        plt.title("Bisektion: Funktion und Intervall")
        plt.xlabel("x-Werte")
        plt.ylabel("f(x)")

        #Diagramm 2: Genauigkeit der Näherung
        plt.subplot(2, 1, 2)
        plt.plot(genauigkeit)
        plt.title("Genauigkeit der Näherung")
        plt.xlabel("Iteration")
        plt.ylabel("|f(c)|")


        plt.tight_layout()
        plt.pause(0.5)

    plt.ioff()
    plt.show()



def solver() -> None:
    """Führt die berechnung und Visualisierung, mit gewünschten zahlwerten
    """
    
    
    funktion = input("Gibt eine Funktion ein: ")
    a = float(input("Gib die erste Intervallsgrenze ein: "))
    b = float(input("Gib die zweite Intervallsgrenze ein: "))

    iterationen = bisektion_iterationen(funktion, a, b)
    plotter(iterationen, funktion, a, b)


if __name__ == "__main__":
    solver()