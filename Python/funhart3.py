# Funzione di HARTMAN (n=3)

import numpy as np

def hartman_function(x):
    # Function to evaluate the HARTMAN function
    a = np.array([[3.0, 0.1, 3.0],
                  [10.0, 10.0, 10.0],
                  [30.0, 35.0, 30.0],
                  [0.1, 10.0, 35.0]])

    c = np.array([1.0, 1.2, 3.0, 3.2])

    p = np.array([[0.3689, 0.4699, 0.1091, 0.03815],
                  [0.1170, 0.4387, 0.8732, 0.5743],
                  [0.2673, 0.7470, 0.5547, 0.8828]])

    f = 0.0
    fa = np.zeros(4)

    for i in range(4):
        for j in range(3):
            fa[i] += a[i, j] * (x[j] - p[i, j])**2
        f -= c[i] * np.exp(-fa[i])

    return f

def hartman_gradient(x):
    # Function to compute the gradient of the HARTMAN function
    a = np.array([[3.0, 0.1, 3.0],
                  [10.0, 10.0, 10.0],
                  [30.0, 35.0, 30.0],
                  [0.1, 10.0, 35.0]])

    c = np.array([1.0, 1.2, 3.0, 3.2])

    p = np.array([[0.3689, 0.4699, 0.1091, 0.03815],
                  [0.1170, 0.4387, 0.8732, 0.5743],
                  [0.2673, 0.7470, 0.5547, 0.8828]])

    fa = np.zeros(4)
    gradient = np.zeros(3)

    for i in range(4):
        for j in range(3):
            fa[i] += a[i, j] * (x[j] - p[i, j])**2

    for i in range(4):
        for j in range(3):
            gradient[j] += c[i] * np.exp(-fa[i]) * 2.0 * a[i, j] * (x[j] - p[i, j])

    return gradient

if __name__ == "__main__":
    # Example usage
    x_example = np.zeros(3)

    function_value = hartman_function(x_example)
    gradient_value = hartman_gradient(x_example)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
