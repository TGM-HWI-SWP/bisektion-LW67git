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
    
def regula_falsi(funktion: str, a: float, b: float, epsilon:float = 0.00001) -> Tuple[float, int]:
    """Nullstelle wird anhand von regula falsi gesucht.
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
            c = b - fb * (b - a)/(fb - fa)
            fc = f(c, funktion)
            iteration += 1

            if abs(fc) <= epsilon:
                return c, iteration
            
            if fa * fc < 0:
                b = c
                fb = fc

            elif fb * fc < 0:
                a = c
                fa = fc

            else:
                raise ValueError("Fehler im Intervall")
    except ValueError as fehler:
        print(f"Fehler: {fehler}")
        return 0, 0
        
def wurzel_regula_falsi_solver(n):
    # Verwendet zum Testen und vergleichen der numerischen Näherung mit der analytischen Lösung der Quadratwurzel von n

    funktion = f"x**2 - {n}"

    a = 0
    b = 2 * n

    näherung, iterationen = regula_falsi(funktion, a, b)
    analytisch = math.sqrt(n)

    print(f"n =     {n}")
    print(f"Näherung:       {näherung}")
    print(f"Exakter Punkt:      {analytisch}")
    print(f"Fehler:     {abs(näherung - analytisch)}")
    print(f"Iterationen:        {iterationen}")
    print("-" * 50)


def solver2(funktion: str = None, a: float = None, b: float = None, epsilon: float = None) -> Tuple[float, int]:
    """Führt das Regula Falsi-Verfahren aus, es kann entweder mit eingabe oder mit übergebenen werten arbeiten.

    Args:
        funktion (str, optional): funktion als string Default as None
        a (float, optional): 1. Intervallsgrenze. Defaults to None.
        b (float, optional): 2. Intervallsgrenze. Defaults to None.
        epsilon (float, optional): Genauigkeit. Defaults to None.

    Returns:
        Tuple[float, int]: Näherung der Nullstelle, Anzahl der Iterationen
    """


    try:
        if funktion is None:
            funktion = input("Gib die Funktion ein: ")
            a = float(input("Gib die erste Intervallsgrenze ein: "))
            b = float(input("Gib die zweite Intervallsgrenze ein: "))
            epsilon = float(input("Gib die Genauigkeit ein: "))

        näherung, iterationen = regula_falsi(funktion, a, b, epsilon)
        
        print("-" * 50)
        print(f"Funktion: f(x) = {funktion}")
        print(f"Näherung: {näherung}")
        print(f"Iterationen: {iterationen}")
        print("-" * 50)

        return näherung, iterationen

    except ValueError as fehler:
        print(f"Fehler: {fehler}")
        return 0,0




if __name__ == "__main__":
    print("Aufgabe 1")
    wurzel_regula_falsi_solver(67)

    print("Aufgabe 2")
    wurzel_regula_falsi_solver(19)

    print("Aufgabe 5.1")
    wurzel_regula_falsi_solver(25)

    print("Aufgabe 5.2")
    wurzel_regula_falsi_solver(81)

    print("Aufgabe 5.3")
    wurzel_regula_falsi_solver(144)

