#=========================================
# Ackley function
#
# n=2 (default)
#   
# molti minimi locali       
#
# valore ottimo della funzione obiettivo = 0.0
#
# punto ottimo = 0
#
#         -15.0 =< x(i) =< 30.0   
#====================================================    

import numpy as np

def ackley_function(x):
    a = 20.0
    b = 0.2
    c = 2.0 * np.pi

    s1 = np.sum(x**2)
    s2 = np.sum(np.cos(c * x))

    f = -a * np.exp(-b * np.sqrt((1.0 / len(x)) * s1)) - np.exp((1.0 / len(x)) * s2) + a + np.exp(1.0)

    return f

def ackley_gradient(x):
    a = 20.0
    b = 0.2
    c = 2.0 * np.pi

    s1 = np.sum(x**2)
    s2 = np.sum(np.cos(c * x))

    g = np.zeros_like(x)

    for i in range(len(x)):
        g[i] = a * b * np.exp(-b * np.sqrt((1.0 / len(x)) * s1)) * (1.0 / np.sqrt((1.0 / len(x)) * s1)) * \
               x[i] * (1.0 / len(x)) + np.exp((1.0 / len(x)) * s2) * np.sin(c * x[i]) * c * (1.0 / len(x))

    return g

def initialize_bounds(n):
    lower_bound = np.full(n, -15.0)
    upper_bound = np.full(n, 30.0)
    return lower_bound, upper_bound

if __name__ == "__main__":
    # Example usage
    n_dim = 2
    x_example = np.zeros(n_dim)

    function_value = ackley_function(x_example)
    gradient_value = ackley_gradient(x_example)
    lower_bound, upper_bound = initialize_bounds(n_dim)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
    print("Lower bounds:", lower_bound)
    print("Upper bounds:", upper_bound)
