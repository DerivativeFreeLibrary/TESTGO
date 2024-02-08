#=========================================
# Easom function
#
# n=2 (default)
#   
# molti minimi locali       
#
# valore ottimo della funzione obiettivo = -1.0
#
# punto ottimo = (pi , pi), 
#
#         -100.0 =< x(i) =< 100.0   
#====================================================   

import numpy as np

def funct(x):
    pi = 3.1415923
    f = -np.cos(x[0]) * np.cos(x[1]) * np.exp(-(x[0] - pi)**2 - (x[1] - pi)**2)
    return f

def data(n):
    l = np.full(n, -100.0)
    u = np.full(n, 100.0)
    fott = -1.0
    return l, u, fott

def grad(x):
    pi = 3.1415923
    g = np.zeros(len(x))

    g[0] = np.sin(x[0]) * np.cos(x[1]) * np.exp(-(x[0] - pi)**2 - (x[1] - pi)**2) - \
           np.cos(x[0]) * np.cos(x[1]) * np.exp(-(x[0] - pi)**2 - (x[1] - pi)**2) * (-2.0 * (x[0] - pi))

    g[1] = np.cos(x[0]) * np.sin(x[1]) * np.exp(-(x[0] - pi)**2 - (x[1] - pi)**2) - \
           np.cos(x[0]) * np.cos(x[1]) * np.exp(-(x[0] - pi)**2 - (x[1] - pi)**2) * (-2.0 * (x[1] - pi))

    return g


if __name__ == "__main__":
    # Example Usage
    n_value = 2
    x_values = np.array([1.0, 2.0])  # Replace with your actual input values

    result_funct = funct(x_values)
    result_data = data(n_value)
    result_grad = grad(x_values)

    print("Result (Function):", result_funct)
    print("Result (Data):", result_data)
    print("Result (Gradient):", result_grad)
