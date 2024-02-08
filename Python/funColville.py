#================================================================
#
# Funzione Colville (n=4) 
#
#================================================================
#				VARIABLE BOUNDS
#================================================================
#       -5.D0                5.D0          Limits of variable 1
#       -5.D0                5.D0          Limits of variable 2
#       -5.D0                5.D0          Limits of variable 3
#       -5.D0                5.D0          Limits of variable 4
# fstar = 0
#================================================================

import numpy as np

def colville_function(x):
    term1 = 100.0 * (x[0]**2 - x[1])**2
    term2 = (x[0] - 1.0)**2
    term3 = (x[2] - 1.0)**2
    term4 = 90.0 * (x[2]**2 - x[3])**2
    term5 = 10.1 * ((x[1] - 1.0)**2 + (x[3] - 1.0)**2)
    term6 = 19.8 * (x[1] - 1.0) * (x[3] - 1.0)

    f = term1 + term2 + term3 + term4 + term5 + term6
    return f

def colville_gradient(x):
    g = np.zeros_like(x)

    g[0] = 400.0 * x[0] * (x[0]**2 - x[1]) + 2.0 * (x[0] - 1.0)
    g[1] = -200.0 * (x[0]**2 - x[1]) + 20.2 * (x[1] - 1.0) + 19.8 * (x[3] - 1.0)
    g[2] = 2.0 * (x[2] - 1.0) + 180.0 * 2.0 * x[2] * (x[2]**2 - x[3])
    g[3] = -180.0 * (x[2]**2 - x[3]) + 20.2 * (x[3] - 1.0) + 19.8 * (x[1] - 1.0)

    return g

if __name__ == "__main__":
    # Example usage
    n_dim = 4
    x_example = np.zeros(n_dim)

    function_value = colville_function(x_example)
    gradient_value = colville_gradient(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
