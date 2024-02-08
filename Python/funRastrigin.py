#===============================================================
#
# Funzione Rastrigin (n variabile) consigliata n=5
# ALI-TORN POPULATION SET BASED GO ALGORITHMS: SOME MODIFICATIONS AND NUMERICAL STUDIES
# COMPUTERS AND OPERATION RESEARCH 
#===============================================================
#			VARIABLE BOUNDS
#===============================================================
#       -5.12D0              5.12D0          Limits of variable i
# FGLOB = 0.0D0 XSTAR = 0.0D0

import numpy as np

def rastrigin_function(x):
    # Function to evaluate the Rastrigin function
    n = len(x)
    x_aux = x + 2.56 * np.sqrt(2.0)
    f = 10.0 * n

    for i in range(n):
        f += x_aux[i]**2 - 10.0 * np.cos(2.0 * np.pi * x_aux[i])

    return f

def rastrigin_gradient(x):
    # Function to compute the gradient of the Rastrigin function
    n = len(x)
    x_aux = x + 2.56 * np.sqrt(2.0)
    g = np.zeros_like(x)

    for i in range(n):
        g[i] = 2.0 * x_aux[i] + 20.0 * np.pi * np.sin(2.0 * np.pi * x_aux[i])

    return g

if __name__ == "__main__":
    # Example usage
    n_dim = 5
    x_example = np.zeros(n_dim)

    function_value = rastrigin_function(x_example)
    gradient_value = rastrigin_gradient(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
