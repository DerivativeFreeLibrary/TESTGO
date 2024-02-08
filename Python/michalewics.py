#=========================================
# Michalewics function
#
# n= variabile
#   
# molti minimi locali       
#
# valore ottimo della funzione obiettivo
#   
#       n=2, f(x*) = -1.8013.
#       n=5, f(x*) = -4.687658.
#       n=10, f(x*) = -9.66015.
#
# punto ottimo = ?
#
#         -pi =< x(i) =< pi   
#====================================================    
import numpy as np

def funct(x):
    pi = 3.1415923
    m = 10
    s = 0.0

    for i in range(1, len(x) + 1):
        s += np.sin(x[i-1]) * (np.sin(float(i) * x[i-1]**2 / pi))**(2*m)

    f = -s
    return f

def data(n):
    pi = 3.1415923
    l = np.full(n, -pi)
    u = np.full(n, pi)

    if n == 2:
        fott = -1.8013
    elif n == 5:
        fott = -4.687658
    elif n == 10:
        fott = -9.66015
    else:
        print("Function Michalewicz is not defined for n =", n)
        raise ValueError("Invalid value of n.")

    return l, u, fott

def grad(x):
    pi = 3.1415923
    m = 10
    g = np.zeros(len(x))

    for i in range(1, len(x) + 1):
        g[i-1] = -np.cos(x[i-1]) * (np.sin(float(i) * x[i-1]**2 / pi))**(2*m) - \
                 np.sin(x[i-1]) * 4.0 * float(m) * float(i) * x[i-1] * \
                 (np.sin(float(i) * (x[i-1]**2) / pi))**(2*m-1) * np.cos(float(i) * (x[i-1]**2) / pi) / pi

    return g


if __name__ == "__main__":
    # Example Usage
    n_value = 10
    x_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])  # Replace with your actual input values

    result_funct = funct(x_values)
    result_data = data(n_value)
    result_grad = grad(x_values)

    print("Result (Function):", result_funct)
    print("Result (Data):", result_data)
    print("Result (Gradient):", result_grad)
