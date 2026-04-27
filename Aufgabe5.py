import math
from typing import Tuple

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
        return eval(funktion)       #eval macht aus dem String eine ausführbare Fuktion, Variable x wird in der Funktion verwendet
    except Exception as fehler:
        raise ValueError(f"Fehler in der Funktion: {fehler}")
    
def bisektion(funktion: str, a: float, b: float, epsilon:float = 0.00001) -> Tuple[float, int]:
    """Nullstelle wird anhand von bisektion gesucht.
    Abbruch, wenn f(c) nahe genug bei 0 ist.

    Args:
        funktion (str): Funktionswert
        a (float): 1. Intervallsgrenze
        b (float): 2. Intervallsgrenze
        epsilon (float, optional): Genauigkeit

    Raises:
        ValueError: Kein gültiges Startintervall
        ValueError: Fehler im Intervall

    Returns:
        Tuple[float, int]: Näherung der Nullstelle, Anzahl der Iterationen
    """


    fa = f(a, funktion)
    fb = f(b, funktion)

    try:
        if fa * fb > 0:
            raise ValueError("Kein gültiges Startintervall")
        
        iteration = 0

        while True:
            c = (a + b) / 2
            fc = f(c, funktion)
            iteration += 1

            if abs(fc) <= epsilon:
                return c, iteration
            
            if fa * fc < 0:
                b = c

            elif fb * fc < 0:
                a = c

            else:
                raise ValueError("Fehler im Intervall")
    except ValueError as fehler:
        print(f"Fehler: {fehler}")
        return 0, 0
        
def wurzel_bisektion(n):

    funktion = f"x**2 - {n}"

    a = 0
    b = 2 * n

    näherung, iterationen = bisektion(funktion, a, b)
    analytisch = math.sqrt(n)

    print(f"n =     {n}")
    print(f"Näherung:       {näherung}")
    print(f"Exakter Punkt:      {analytisch}")
    print(f"Fehler:     {abs(näherung - analytisch)}")
    print(f"Iterationen:        {iterationen}")
    print("-" * 50)


def solver():
    wurzel_bisektion(25)
    wurzel_bisektion(81)
    wurzel_bisektion(144)


if __name__ == "__main__":
    
    solver()