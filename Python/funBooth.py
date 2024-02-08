#====================================
# Booth function
# n = 2
# -10 <= x <= 10
# fstar = 0
#====================================

import numpy as np

def booth_function(x):
    A = x[0] + 2.0 * x[1] - 7.0
    B = 2.0 * x[0] + x[1] - 5.0
    f = A**2 + B**2
    return f

def booth_gradient(x):
    A = x[0] + 2.0 * x[1] - 7.0
    B = 2.0 * x[0] + x[1] - 5.0
    g = np.array([2.0 * A + 4.0 * B, 4.0 * A + 2.0 * B])
    return g

if __name__ == "__main__":
    # Example usage
    n_dim = 2
    x_example = np.zeros(n_dim)

    function_value = booth_function(x_example)
    gradient_value = booth_gradient(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
