# Funzione di HARTMAN (n=6)

import numpy as np

def hartman_function_6(x):
    # Function to evaluate the HARTMAN function with n=6
    a = np.array([[10.0, 0.05, 3.0, 17.0, 3.5, 8.0],
                  [3.0, 10.0, 3.5, 8.0, 17.0, 14.0]])

    c = np.array([1.0, 1.2, 3.0, 3.2])

    p = np.array([[0.1312, 0.2329, 0.2348, 0.4047],
                  [0.1696, 0.4135, 0.1451, 0.8828],
                  [0.5569, 0.8307, 0.3522, 0.8732],
                  [0.0124, 0.3736, 0.2883, 0.5743],
                  [0.8283, 0.1004, 0.3047, 0.1091],
                  [0.5886, 0.9991, 0.6650, 0.0381]])

    f = 0.0
    fa = np.zeros(4)

    for i in range(4):
        for j in range(6):
            fa[i] += a[i, j] * (x[j] - p[i, j])**2
        f -= c[i] * np.exp(-fa[i])

    return f

def hartman_gradient_6(x):
    # Function to compute the gradient of the HARTMAN function with n=6
    a = np.array([[10.0, 0.05, 3.0, 17.0, 3.5, 8.0],
                  [3.0, 10.0, 3.5, 8.0, 17.0, 14.0]])

    c = np.array([1.0, 1.2, 3.0, 3.2])

    p = np.array([[0.1312, 0.2329, 0.2348, 0.4047],
                  [0.1696, 0.4135, 0.1451, 0.8828],
                  [0.5569, 0.8307, 0.3522, 0.8732],
                  [0.0124, 0.3736, 0.2883, 0.5743],
                  [0.8283, 0.1004, 0.3047, 0.1091],
                  [0.5886, 0.9991, 0.6650, 0.0381]])

    fa = np.zeros(4)
    gradient = np.zeros(6)

    for i in range(4):
        for j in range(6):
            fa[i] += a[i, j] * (x[j] - p[i, j])**2

    for i in range(4):
        for j in range(6):
            gradient[j] += c[i] * np.exp(-fa[i]) * 2.0 * a[i, j] * (x[j] - p[i, j])

    return gradient

if __name__ == "__main__":
    # Example usage
    x_example = np.zeros(6)

    function_value = hartman_function_6(x_example)
    gradient_value = hartman_gradient_6(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
