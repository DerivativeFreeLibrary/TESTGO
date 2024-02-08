#=========================================
# Dixon & Price function
#
# n= variabile (25 (default))
#        
# valore ottimo della funzione obiettivo = 0.0
#
#         -10.0 =< x(i) =< 10.0   
#====================================================    

import numpy as np

def funct(x):
    n = len(x)
    f = 0.0

    for i in range(2, n+1):
        f += float(i) * (2.0 * x[i-1]**2 - x[i-2])**2

    f += (x[0] - 1.0)**2

    return f

def data(n):
    l = np.full(n, -10.0)
    u = np.full(n, 10.0)
    fott = 0.0

    return l, u, fott

def grad(n, x):
    g = np.zeros(n)

    for i in range(1, n+1):
        if i == 1:
            g[0] = 2.0 * (x[0] - 1.0) - 2.0 * float(i + 1) * (2.0 * x[1]**2 - x[0])
        elif i < n:
            g[i-1] = 8.0 * float(i) * x[i-1] * (2.0 * x[i-1]**2 - x[i-2]) - 2.0 * float(i + 1) * (2.0 * x[i]**2 - x[i-1])
        else:
            g[i-1] = 8.0 * float(i) * x[i-1] * (2.0 * x[i-1]**2 - x[i-2])

    return g


if __name__ == "__main__":
    # Example Usage
    n_value = 25
    x_values = np.random.uniform(-10.0, 10.0, n_value)  # Replace with your actual input values

    result_funct = funct(x_values)
    result_data = data(n_value)
    result_grad = grad(n_value, x_values)

    print("Result (Function):", result_funct)
    print("Result (Data):", result_data)
    print("Result (Gradient):", result_grad)
