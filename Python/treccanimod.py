#=========================================
#
# FUNZIONE DI TRECCANI
# 
#  X(1) .GE. -2.5  ;  X(2) .LE.  2.5
#
#=========================================

import numpy as np

def funct(x):
    x_aux = x + 0.25 * np.sqrt(2.0)
    x1q = x_aux[0] * x_aux[0]
    result = x1q * x1q + 4.0 * x1q * x_aux[0] + 4.0 * x1q + x_aux[1] * x_aux[1]
    return result

def grad(x):
    x_aux = x + 0.25 * np.sqrt(2.0)

    g1 = 4.0 * x_aux[0]**3 + 12.0 * x_aux[0]**2 + 8.0 * x_aux[0]
    g2 = 2.0 * x_aux[1]

    return np.array([g1, g2])

if __name__ == "__main__":
    # Example Usage
    n_value = 2
    x_values = np.array([1.0, 2.0])  # Replace with your actual input values

    result_funct = funct(x_values)
    result_grad = grad(x_values)

    print("Result (Function):", result_funct)
    print("Result (Gradient):", result_grad)
