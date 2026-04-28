import matplotlib.pyplot as plt
import numpy as np

def f(x: float, funktion: str) -> float:
    """Berechnet den Funktionswert für eine gegebene Funktion und Variable x

    Args:
        x (float): Funktionsvariable
        funktion (str): Funktion als string

    Raises:
        ValueError: Bei Fehler in der Funktion wird ein ValueError mit einer Fehlermeldung ausgelöst

    Returns:
        float: Funktionswert wird als float zurückgegeben
    """

    try:
        return eval(funktion)
    except Exception as fehler:
        raise ValueError(f"Fehler in der Funktion: {fehler}")


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

        iterationen.append((a, b, c, fc))

        if abs(fc) <= epsilon:
            break

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
    genaugkeit = []

    x = np.linspace(a, b, 500)
    y = [f(xi, funktion) for xi in x]

    plt.ion()

    for a, b, c, fc in iterationen:
        lösung.append(c)
        genaugkeit.append(abs(fc))

        plt.clf()

        plt.subplot(3, 1, 1)
        plt.plot(x,y)
        plt.axhline(0, color='red', linestyle='--')
        plt.axvline(c, color='green', linestyle='--')
        plt.axvline(a, color='blue', linestyle='--')
        plt.axvline(b, color='orange', linestyle='--')
        plt.title("Bisektion: Funktion und Intervall")

        plt.subplot(3, 1, 2)
        plt.plot(genaugkeit)
        plt.title("Genauigkeit der Näherung")

        plt.subplot(3, 1, 3)
        plt.plot(lösung)
        plt.title("Näherung der Nullstelle")

        plt.tight_layout()
        plt.pause(0.5)

    plt.ioff()
    plt.show()



def solver() -> None:
    """Führt die berechnung und Visualisierung, mit gewünschten zahlwerten
    """
    
    
    funktion = "x**2 - 67"
    a = 0
    b = 2 * 67
    
    iterationen = bisektion_iterationen(funktion, a, b)
    plotter(iterationen, funktion, a, b)


if __name__ == "__main__":
    solver()