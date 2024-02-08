# ! FUNZIONE DI GRIEWANK (intervallo ??)


import numpy as np

def funct(x):
    n = len(x)
    xaux = x + 5.0 * np.sqrt(2.0)

    f = 1.0

    for i in range(1, n+1):
        f *= np.cos(xaux[i-1] / np.sqrt(float(i)))

    f = -f + 1.0

    for i in range(1, n+1):
        f += xaux[i-1] * xaux[i-1] / 4.0 + 3.0

    return f

def grad(x):
    n = len(x)
    xaux = x + 5.0 * np.sqrt(2.0)
    prod = np.ones(n)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                prod[i-1] *= np.cos(xaux[j-1] / np.sqrt(float(j)))

    g = np.zeros(n)

    for i in range(1, n+1):
        g[i-1] = (2.0 * xaux[i-1]) / 4.0 + 3.0 / np.sqrt(float(i)) * np.sin(xaux[i-1] / np.sqrt(float(i))) * prod[i-1]

    return g

if __name__ == "__main__":
    # Example Usage
    n_value = 5
    x_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0])  # Replace with your actual input values

    result_funct = funct(x_values)
    result_grad = grad(x_values)

    print("Result (Function):", result_funct)
    print("Result (Gradient):", result_grad)
