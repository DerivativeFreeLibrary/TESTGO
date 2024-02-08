
# schwefel function
# -500 <= x <= 500
# fstar = 0
#--------------------
#     SCHWEFEL FUNCTION
#--------------------

import numpy as np

def funct(x):
    n = len(x)
    f = 418.9828873 * n

    for k in range(n):
        f -= x[k] * np.sin(np.sqrt(np.abs(x[k])))

    return f

def grad(x):
    n = len(x)
    g = np.zeros(n)

    for k in range(n):
        rd = np.sqrt(np.abs(x[k]))
        g[k] = -np.sin(rd) - 0.5 * rd * np.cos(rd)

    return g


if __name__ == "__main__":
    # Example Usage
    n_value = 3
    x_values = np.array([100.0, 200.0, -300.0])  # Replace with your actual input values

    result_funct = funct(x_values)
    result_grad = grad(x_values)

    print("Result (Function):", result_funct)
    print("Result (Gradient):", result_grad)
