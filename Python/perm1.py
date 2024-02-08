# Perm function 1
# -n <= x <= n
# fstar = 0
#--------------------
#     PERM1 FUNCTION
#--------------------

import numpy as np

def perm1_function(x):
    # PERM1 function
    n = len(x)
    f = 0.0

    for k in range(1, n + 1):
        s = 0.0
        for j in range(1, n + 1):
            s += (j**k + 0.5) * ((x[j-1]/j)**k - 1.0)
        f += s**2

    return f

def perm1_gradient(x):
    # Gradient of the PERM1 function
    n = len(x)
    g = np.zeros(n)
    s1 = 0.0

    for j in range(1, n + 1):
        s1 += (j + 0.5) * ((x[j-1]/j) - 1.0)

    for i in range(1, n + 1):
        g[i-1] = 2.0 * s1 * (i + 0.5) / i

        for k in range(2, n + 1):
            s = 0.0
            for j in range(1, n + 1):
                s += (j**k + 0.5) * ((x[j-1]/j)**k - 1.0)
            
            g[i-1] += 2.0 * s * k * (i**k + 0.5) * ((x[i-1]/i)**(k-1) / i)

    return g

if __name__ == "__main__":
    # Example usage
    x_example = np.zeros(4)

    function_value = perm1_function(x_example)
    gradient_value = perm1_gradient(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
