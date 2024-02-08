# Funzione Cosine Mixture

import numpy as np

def cosine_mixture_function(x):
    # Function to evaluate the Cosine Mixture function
    n = len(x)
    x_aux = x + 0.5 * np.sqrt(2.0)
    f = 0.0

    for i in range(n):
        f += 0.1 * np.cos(5.0 * np.pi * x_aux[i]) - x_aux[i]**2

    return -f  # Note: Negative because the Fortran code has a minus sign

def cosine_mixture_gradient(x):
    # Function to compute the gradient of the Cosine Mixture function
    n = len(x)
    x_aux = x + 0.5 * np.sqrt(2.0)
    g = np.zeros_like(x)

    for i in range(n):
        g[i] = 0.1 * np.sin(5.0 * np.pi * x_aux[i]) * 5.0 * np.pi + 2.0 * x_aux[i]

    return -g  # Note: Negative because the Fortran code has a minus sign

if __name__ == "__main__":
    # Example usage
    n_dim = 5
    x_example = np.zeros(n_dim)

    function_value = cosine_mixture_function(x_example)
    gradient_value = cosine_mixture_gradient(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
