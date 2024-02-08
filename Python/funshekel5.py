#=========================================
#
# Funzione di Shekel 5 minimi (n=4) 
#
#=========================================

import numpy as np

def shekel_function_5(x):
    # Function to evaluate the Shekel function with 5 minima (n=4)
    a = np.zeros((5, 4))
    c = np.zeros(5)
    fa = 0.0

    for i in range(4):
        a[0:4, i] = [4.0, 1.0, 8.0, 6.0]

    for i in range(2):
        a[4, 2 * i] = 3.0
        a[4, 2 * i + 1] = 7.0

    c[0:5] = [0.1, 0.2, 0.2, 0.4, 0.4]

    f = 0.0

    for i in range(5):
        for j in range(4):
            fa += (x[j] - a[i, j]) ** 2

        if (fa + c[i]) == 0.0:
            return 1e25

        f -= 1.0 / (fa + c[i])
        fa = 0.0

    return f

def shekel_gradient_5(x):
    # Function to compute the gradient of the Shekel function with 5 minima (n=4)
    a = np.zeros((5, 4))
    c = np.zeros(5)
    fa = 0.0
    gradient = np.zeros(4)

    for i in range(4):
        a[0:4, i] = [4.0, 1.0, 8.0, 6.0]

    for i in range(2):
        a[4, 2 * i] = 3.0
        a[4, 2 * i + 1] = 7.0

    c[0:5] = [0.1, 0.2, 0.2, 0.4, 0.4]

    fa = 0.0
    gradient = np.zeros(4)

    for i in range(5):
        for j in range(4):
            fa += (x[j] - a[i, j]) ** 2

        for j in range(4):
            gradient[j] += 2.0 * (x[j] - a[i, j]) / (fa + c[i]) ** 2

        fa = 0.0

    return gradient

if __name__ == "__main__":
    # Example usage
    x_example = np.zeros(4)

    function_value = shekel_function_5(x_example)
    gradient_value = shekel_gradient_5(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
