# Perm function 2
# -n <= x <= n
# fstar = 0
#--------------------
#     PERM2 FUNCTION
#--------------------
import numpy as np

def perm2_function(x):
    # PERM2 function
    n = len(x)
    f = 0.0

    for k in range(1, n + 1):
        s = 0.0
        for j in range(1, n + 1):
            s += (j + 10.0) * (x[j-1]**k - (1.0/j)**k)
        f += s**2

    return f

def perm2_gradient(x):
    # Gradient of the PERM2 function
    n = len(x)
    g = np.zeros(n)
    s1 = 0.0

    for j in range(1, n + 1):
        s1 += (j + 10.0) * (x[j-1] - 1.0/j)

    for i in range(1, n + 1):
        g[i-1] = 2.0 * s1 * (i + 10.0)

        for k in range(2, n + 1):
            s = 0.0
            for j in range(1, n + 1):
                s += (j + 10.0) * (x[j-1]**k - (1.0/j)**k)
            
            g[i-1] += 2.0 * s * k * (i + 10.0) * x[i-1]**(k - 1)

    return g

if __name__ == "__main__":
    # Example usage
    x_example = np.zeros(4)

    function_value = perm2_function(x_example)
    gradient_value = perm2_gradient(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
