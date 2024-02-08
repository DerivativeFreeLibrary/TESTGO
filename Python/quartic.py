#*************************************************
#	FUNZIONE ZIRILLI2
#*************************************************

import numpy as np

def funct(x):
    f = (1./4.) * x[0]**4 - (1./2.) * x[0]**2 + 0.1 * x[0] + (1./2.) * x[1]**2
    return f

def grad(x):
    g = np.zeros(len(x))
    g[0] = x[0]**3 - x[0] + 0.1
    g[1] = x[1]
    return g

def hess(x):
    h = np.array([[3.0 * x[0]**2 - 1.0, 0.0],
                  [0.0, 1.0]])
    return h

def hesdir(x, d):
    h = hess(x)
    hd = np.dot(h, d)
    return hd

if __name__ == "__main__":

    # Example Usage
    n_value = 2
    x_values = np.array([1.0, 2.0])  # Replace with your actual input values
    direction_values = np.array([0.5, 0.8])  # Replace with your actual direction values

    result_funct = funct(x_values)
    result_grad = grad(x_values)
    result_hess = hess(x_values)
    result_hesdir = hesdir(x_values, direction_values)

    print("Result (Function):", result_funct)
    print("Result (Gradient):", result_grad)
    print("Result (Hessian):", result_hess)
    print("Result (Hessian x Direction):", result_hesdir)
