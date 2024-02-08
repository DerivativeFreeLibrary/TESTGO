#*************************************************
#	FUNZIONE CAMEL
#*************************************************
import numpy as np

def camel_function(x):
    f = (4.0 - 2.1 * x[0]**2 + (x[0]**4) / 3.0) * x[0]**2 + x[0] * x[1] + (-4.0 + 4.0 * x[1]**2) * x[1]**2
    return f

def camel_gradient(x):
    g = np.zeros_like(x)
    g[0] = x[1] + 8.0 * x[0] - 8.4 * x[0]**3 + 2.0 * x[0]**5
    g[1] = x[0] - 8.0 * x[1] + 16.0 * x[1]**3
    return g

def camel_hessian(x):
    h = np.zeros((len(x), len(x)))
    h[0, 0] = 8.0 - 25.2 * x[0]**2 + 10.0 * x[0]**4
    h[0, 1] = 1.0
    h[1, 0] = h[0, 1]
    h[1, 1] = -8.0 + 48.0 * x[1]**2
    return h

def camel_hessian_direction(x, d):
    h = camel_hessian(x)
    hd = np.dot(h, d)
    return hd

if __name__ == "__main__":
    # Example usage
    n_dim = 2
    x_example = np.zeros(n_dim)

    function_value = camel_function(x_example)
    gradient_value = camel_gradient(x_example)
    hessian_value = camel_hessian(x_example)
    direction = np.array([1.0, 1.0])  # Example direction
    hessian_direction_value = camel_hessian_direction(x_example, direction)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
    print("Hessian value:\n", hessian_value)
    print("Hessian x Direction value:", hessian_direction_value)
