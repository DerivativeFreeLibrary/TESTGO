# Funzione Esponenziale

import numpy as np

def exponential_function(x):
    # Function to evaluate the Exponential function
    n = len(x)
    x_aux = x + 0.5 * np.sqrt(2.0)
    f1 = 0.0

    for i in range(n):
        f1 += x_aux[i]**2

    f = -np.exp(-0.5 * f1)

    return f

def exponential_gradient(x):
    # Function to compute the gradient of the Exponential function
    n = len(x)
    x_aux = x + 0.5 * np.sqrt(2.0)
    f1 = 0.0

    for i in range(n):
        f1 += x_aux[i]**2

    g = -np.exp(-0.5 * f1) * x_aux

    return g

if __name__ == "__main__":
    # Example usage
    n_dim = 5
    x_example = np.zeros(n_dim)

    function_value = exponential_function(x_example)
    gradient_value = exponential_gradient(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
