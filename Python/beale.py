# n = 2
# -4.5 <= x <= 4.5
# fstar = 0
#**************************************************
#	FUNZIONE BEALE
#**************************************************

import numpy as np

def startp():
    x = np.zeros(2)
    x[0] = 1.0
    x[1] = 1.0
    return x

def funct(x):
    y = np.array([1.5, 2.25, 2.625])
    
    if abs(1.0 - x[1]) > 1.0e-16 or abs(x[0]) > 1.0e5 or abs(x[1]) > 1.0e5:
        return 1.0e34
    
    f = (y[0] - x[0] * (1.0 - x[1]))**2
    f += (y[1] - x[0] * (1.0 - x[1]**2))**2
    f += (y[2] - x[0] * (1.0 - x[1]**3))**2
    
    return f

def grad(x):
    y = np.array([1.5, 2.25, 2.625])
    g = np.zeros(2)

    g[0] = -2.0 * (y[0] - x[0] * (1.0 - x[1])) * (1.0 - x[1])
    g[0] -= 2.0 * (y[1] - x[0] * (1.0 - x[1]**2)) * (1.0 - x[1]**2)
    g[0] -= 2.0 * (y[2] - x[0] * (1.0 - x[1]**3)) * (1.0 - x[1]**3)

    g[1] = 2.0 * (y[0] - x[0] * (1.0 - x[1])) * x[0]
    g[1] += 2.0 * (y[1] - x[0] * (1.0 - x[1]**2)) * (2.0 * x[0] * x[1])
    g[1] += 2.0 * (y[2] - x[0] * (1.0 - x[1]**3)) * (3.0 * x[0] * x[1]**2)

    return g

def hess(x):
    y = np.array([1.5, 2.25, 2.625])
    h = np.zeros((2, 2))

    h[0, 0] = 2.0 * (1.0 - x[1]) * (1.0 - x[1])
    h[0, 0] += 2.0 * (1.0 - x[1]**2) * (1.0 - x[1]**2)
    h[0, 0] += 2.0 * (1.0 - x[1]**3) * (1.0 - x[1]**3)

    h[1, 1] = 2.0 * x[0] * x[0]
    h[1, 1] += 2.0 * (2.0 * x[0] * x[1])**2 + 2.0 * (y[1] - x[0] * (1.0 - x[1]**2)) * (2.0 * x[0])
    h[1, 1] += 2.0 * (3.0 * x[0] * x[1]**2)**2 + 2.0 * (y[2] - x[0] * (1.0 - x[1]**3)) * (6.0 * x[0] * x[1])

    h[0, 1] = -2.0 * (1.0 - x[1]) * x[0] + 2.0 * (y[0] - x[0] * (1.0 - x[1]))
    h[0, 1] -= 2.0 * (1.0 - x[1]**2) * (2.0 * x[0] * x[1]) + 2.0 * (y[1] - x[0] * (1.0 - x[1]**2)) * (2.0 * x[1])
    h[0, 1] -= 2.0 * (1.0 - x[1]**3) * (3.0 * x[0] * x[1]**2) + 2.0 * (y[2] - x[0] * (1.0 - x[1]**3)) * (3.0 * x[1]**2)

    h[1, 0] = h[0, 1]

    return h

def hesdir(x, d):
    h = hess(x)
    hd = np.dot(h, d)
    return hd


if __name__ == '__main__':
    # Example Usage
    x_initial = startp()
    print("Initial x:", x_initial)

    # Call the function FUNCT
    result_funct = funct(x_initial)
    print("Result (FUNCT):", result_funct)

    # Call the function GRAD
    result_grad = grad(x_initial)
    print("Result (GRAD):", result_grad)

    # Call the function HESS
    result_hess = hess(x_initial)
    print("Result (HESS):")
    print(result_hess)

    # Example Direction vector
    direction_vector = np.array([0.1, 0.2])

    # Call the function HESDIR
    result_hesdir = hesdir(x_initial, direction_vector)
    print("Result (HESDIR):", result_hesdir)
