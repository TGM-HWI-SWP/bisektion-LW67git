from Aufgabe5 import solver


def solver_aufgabe8() -> None:
    """Testet das Bisektionsverfahren mit dem Polynom f(x) = 2*x + x**2 + 3*x**3 - x**4 im Intervall [3, 4] und verschiedenen Genauigkeiten

        Returns: None
    """

    funktion = "2*x + x**2 + 3*x**3 - x**4"
    a = 3
    b = 4

    
    print("-" * 50 )
    print("Genauigkeit: 0.01")
    solver(funktion, a, b, epsilon=0.01)
    print("-" * 50)

    print("Genauigkeit: 0.00000001")
    solver(funktion, a, b, epsilon=0.00000001)
    print("-" * 50)


if __name__ == "__main__":
    solver_aufgabe8()