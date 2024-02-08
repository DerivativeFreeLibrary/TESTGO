#====================================
# Bohachevsky Function 1
# n = 2
# -100 <= x <= 100
# fstar = 0
#====================================

import numpy as np

def bohachevsky_function_1(x):
    xx = x + 5.0 * np.sqrt(2.0)
    f = xx[0]**2 + 2.0 * xx[1]**2 - 0.3 * np.cos(3.0 * np.pi * xx[0])
    f = f - 0.4 * np.cos(4.0 * np.pi * xx[1]) + 0.7
    return f

def bohachevsky_gradient_1(x):
    xx = x + 5.0 * np.sqrt(2.0)
    g = np.zeros_like(x)
    g[0] = 2.0 * xx[0] + 0.9 * np.pi * np.sin(3.0 * np.pi * xx[0])
    g[1] = 4.0 * (xx[1] + 0.4 * np.pi * np.sin(4.0 * np.pi * xx[1]))
    return g

if __name__ == "__main__":
    # Example usage
    n_dim = 2
    x_example = np.zeros(n_dim)

    function_value = bohachevsky_function_1(x_example)
    gradient_value = bohachevsky_gradient_1(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
