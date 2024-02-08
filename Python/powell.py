
# -4 <= x <= 5
# fstar = 0
#--------------------
#     POWELL FUNCTION
#--------------------
import numpy as np

def funct(x):
    n = len(x)
    m = n // 4
    y = np.zeros((m, 4))
    f = 0.0

    for k in range(1, m+1):
        for j in range(1, 5):
            y[k-1, j-1] = x[j + 4*(k-1)-1]

        f += (y[k-1, 0] + 10.0 * y[k-1, 1])**2 + 5.0 * (y[k-1, 2] - y[k-1, 3])**2 \
             + (y[k-1, 1] - 2.0 * y[k-1, 2])**4 + 10.0 * (y[k-1, 0] - y[k-1, 3])**4

    return f

def grad(x):
    n = len(x)
    m = n // 4
    y = np.zeros((m, 4))
    g = np.zeros(n)
    gy = np.zeros(4)

    for k in range(1, m+1):
        for j in range(1, 5):
            y[k-1, j-1] = x[j + 4*(k-1)-1]

        gy[0] = 2.0 * (y[k-1, 0] + 10.0 * y[k-1, 1]) + 40.0 * (y[k-1, 0] - y[k-1, 3])**3
        gy[1] = 20.0 * (y[k-1, 0] + 10.0 * y[k-1, 1]) + 4.0 * (y[k-1, 1] - 2.0 * y[k-1, 2])**3
        gy[2] = 10.0 * (y[k-1, 2] - y[k-1, 3]) - 8.0 * (y[k-1, 1] - 2.0 * y[k-1, 2])**3
        gy[3] = -10.0 * (y[k-1, 2] - y[k-1, 3]) - 40.0 * (y[k-1, 0] - y[k-1, 3])**3

        for j in range(1, 5):
            g[j + 4*(k-1)-1] = gy[j-1]

    return g

if __name__ == "__main__":
    # Example Usage
    n_value = 12
    x_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0])  # Replace with your actual input values

    result_funct = funct(x_values)
    result_grad = grad(x_values)

    print("Result (Function):", result_funct)
    print("Result (Gradient):", result_grad)
