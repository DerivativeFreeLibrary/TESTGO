#===============================================================
#
# FUNZIONE DI PINTER (n=2,5,10,20,....)
# HANDBOOK OF GLOBAL OPTIMIZATION VOLUME 2 CAPITOLO 15 DI PINTER
#
#===============================================================
#			VARIABLE BOUNDS
#===============================================================
#       -5.D+0               5.D+0        Limits of variable i

import numpy as np

def pinter_function(x):
    n = len(x)
    xstar = np.zeros(n)

    for i in range(1, n + 1):
        if i % 2 == 0:
            xstar[i-1] = (i / n) * 4.0 - 0.5
        else:
            xstar[i-1] = -(i / n) * 4.0 + 0.5

    f = 0.0
    for i in range(1, n + 1):
        f += 0.025 * n * (x[i-1] - xstar[i-1])**2

    p1 = 0.0
    p2 = 0.0
    for i in range(1, n + 1):
        p1 += (x[i-1] - xstar[i-1]) + (x[i-1] - xstar[i-1])**2
        p2 += (x[i-1] - xstar[i-1])

    f += np.sin(p1)**2 + np.sin(p2)**2

    return f

def pinter_gradient(x):
    n = len(x)
    xstar = np.zeros(n)
    g = np.zeros(n)
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            xstar[i-1] = (i / n) * 4.0 - 0.5
        else:
            xstar[i-1] = -(i / n) * 4.0 + 0.5

    p = 0.0
    pq = 0.0

    for i in range(1, n + 1):
        p += x[i-1] - xstar[i-1]
        pq += (x[i-1] - xstar[i-1])**2

    s = 0.025 * n

    for i in range(1, n + 1):
        g[i-1] = 2.0 * s * (x[i-1] - xstar[i-1]) + 2.0 * np.sin(p + pq) * np.cos(p + pq) * (1.0 + 2.0 * (x[i-1] - xstar[i-1])) \
                 + 2.0 * np.sin(p) * np.cos(p)

    return g

if __name__ == "__main__":
    # Example usage
    x_example = np.zeros(5)

    function_value = pinter_function(x_example)
    gradient_value = pinter_gradient(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
