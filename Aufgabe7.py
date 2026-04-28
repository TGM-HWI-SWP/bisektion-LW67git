import matplotlib.pyplot as plt
import numpy as np

def f(x, funktion):
    try:
        return eval(funktion)
    except Exception as fehler:
        raise ValueError(f"Fehler in der Funktion: {fehler}")


def bisektion_iterationen(funktion, a, b, epsilon = 0.000001):
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
    

def plotter(iterationen, funktion, a, b):
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



if __name__ == "__main__":
    funktion = "x**2 - 67"
    a = 0
    b = 2 * 67
    
    iterationen = bisektion_iterationen(funktion, a, b)
    plotter(iterationen, funktion, a, b)