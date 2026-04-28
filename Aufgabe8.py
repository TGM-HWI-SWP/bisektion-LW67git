from Aufgabe5 import bisektion


def solver() -> None:
    """Testet das Bisektionsverfahren mit der Funktion f(x) = 2*x + x**2 + 3*x**3 - x**4 im Intervall [3, 4] und verschiedenen Genauigkeiten
    """
    funktion = "2*x + x**2 + 3*x**3 - x**4"
    a = 3
    b = 4
    näherung1, iterationen1 = bisektion(funktion, a, b, epsilon=0.01)

    näherung2, iterationen2 = bisektion(funktion, a, b, epsilon=0.000001)

    print("-" * 50 )
    print("Funktion: f(x) = 2*x + x**2 + 3*x**3 - x**4")
    
    print("-" * 50 )
    print("Genauigkeit: 0.01")
    print(f"Näherung: {näherung1}, Iterationen: {iterationen1}")
    print("-" * 50)

    print("Genauigkeit: 0.000001")
    print(f"Näherung: {näherung2}, Iterationen: {iterationen2}")
    print("-" * 50)


if __name__ == "__main__":
    solver()