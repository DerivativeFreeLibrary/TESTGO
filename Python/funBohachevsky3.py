#====================================
# Bohachevsky Function 3
# n = 2
# -100 <= x <= 100
# fstar = 0
#====================================

import numpy as np

def bohachevsky_function_3(xx):
    x = xx + 5.0 * np.sqrt(2.0)
    f = x[0]**2 + 2.0 * x[1]**2 - 0.3 * np.cos(3.0 * np.pi * x[0] + 4.0 * np.pi * x[1]) + 0.3
    return f

def bohachevsky_gradient_3(y):
    x = y + 5.0 * np.sqrt(2.0)
    g = np.zeros_like(y)
    g[0] = 2.0 * x[0] + 0.3 * 3.0 * np.pi * np.sin(3.0 * np.pi * x[0] + 4.0 * np.pi * x[1])
    g[1] = 4.0 * x[1] + 0.3 * 4.0 * np.pi * np.sin(3.0 * np.pi * x[0] + 4.0 * np.pi * x[1])
    return g

if __name__ == "__main__":
    # Example usage
    n_dim = 2
    xx_example = np.zeros(n_dim)

    function_value = bohachevsky_function_3(xx_example)
    gradient_value = bohachevsky_gradient_3(xx_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
