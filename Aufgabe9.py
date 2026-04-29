from Aufgabe5 import solver
from Aufgabe6 import solver2
import math


def solver_aufgabe9() -> None:
    """Berechnet den Krümmungsradius einer Kettenlinie und die Länge des Seils, mithilfe vom Bisektionsverfahren und Regula Falsi-Verfahren (Überprüfung)
    
    Returns: None
    """


    print("-" * 50)
    print("Mit solver (Bisektionsverfahren):")
    funktion = "x * math.cosh(50/x) - x -10"
    

    a = 50
    b = 150
    epsilon = 0.00001

    radius, iterationen = solver(funktion, a, b, epsilon)

    w = 100

    länge = 2 * radius * math.sinh(w/(2*radius))

    print(f"Radius: {radius}")
    print(f"Anzahl der Iterationen: {iterationen}")
    print(f"Länge des Seils: {länge}")
    print("-" * 50)
    print("-" * 50)
    print("-" * 50)

    print("Mit solver2 (Regula Falsi):")
    
    radius, iterationen = solver2(funktion, a, b, epsilon)

    länge = 2 * radius * math.sinh(w/(2*radius))

    print(f"Radius: {radius}")
    print(f"Anzahl der Iterationen: {iterationen}")
    print(f"Länge des Seils: {länge}")
    print("-" * 50)


if __name__ == "__main__":
    solver_aufgabe9()