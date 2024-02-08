#*************************************************
#	FUNZIONE ZIRILLI 14
#*************************************************
import numpy as np

def zirilli14_function(x):
    pg = np.arccos(-1.0)
    cost = 0.1
    nm = len(x) - 1

    f = np.sin(3.0 * pg * x[0])**2

    for i in range(nm):
        ip = i + 1
        f += (x[i] - 1.0)**2 * (1.0 + np.sin(3.0 * pg * x[ip])**2)

    f += (x[-1] - 1.0)**2
    f *= cost

    return f

def zirilli14_gradient(x):
    pg = np.arccos(-1.0)
    cost = 0.1
    nm = len(x) - 1

    g = np.zeros_like(x)

    g[0] = 6.0 * np.sin(3.0 * pg * x[0]) * np.cos(3.0 * pg * x[0]) * pg
    g[0] += 2.0 * (x[0] - 1.0) * (1.0 + np.sin(3.0 * pg * x[1])**2)
    g[0] *= cost

    for i in range(1, nm):
        im = i - 1
        ip = i + 1

        g[i] = 6.0 * (x[im] - 1.0)**2 * np.sin(3.0 * pg * x[i]) * np.cos(3.0 * pg * x[i]) * pg
        g[i] += 2.0 * (x[i] - 1.0) * (1.0 + np.sin(3.0 * pg * x[ip])**2)
        g[i] *= cost

    g[-1] = 6.0 * (x[nm - 1] - 1.0)**2 * np.sin(3.0 * pg * x[-1]) * np.cos(3.0 * pg * x[-1]) * pg
    g[-1] += 2.0 * (x[-1] - 1.0) * (1.0 + np.sin(2.0 * pg * x[-1])**2)
    g[-1] += 8.0 * (x[-1] - 1.0) * np.sin(2.0 * pg * x[-1]) * np.cos(2.0 * pg * x[-1]) * pg
    g[-1] += 8.0 * (x[-1] - 1.0) * np.sin(2.0 * pg * x[-1]) * np.cos(2.0 * pg * x[-1]) * pg
    g[-1] += 8.0 * pg**2 * (x[-1] - 1.0)**2 * (np.cos(2.0 * pg * x[-1])**2 - np.sin(2.0 * pg * x[-1])**2)
    g[-1] *= cost

    return g

def zirilli14_hessian(x):
    pg = np.arccos(-1.0)
    cost = 0.1
    nm = len(x) - 1

    h = np.zeros((len(x), len(x)))

    h[0, 0] = 18.0 * pg**2 * (np.cos(3.0 * pg * x[0])**2 - np.sin(3.0 * pg * x[0])**2)
    h[0, 0] += 2.0 * (1.0 + np.sin(3.0 * pg * x[1])**2)
    h[0, 0] *= cost

    h[0, 1] = 12.0 * pg * (x[0] - 1.0) * np.sin(3.0 * pg * x[1]) * np.cos(3.0 * pg * x[1])
    h[0, 1] *= cost

    h[1, 0] = h[0, 1]

    for i in range(1, nm):
        ip = i + 1
        im = i - 1

        h[i, i] = 18.0 * pg**2 * (x[im] - 1.0)**2 * (np.cos(3.0 * pg * x[i])**2 - np.sin(3.0 * pg * x[i])**2)
        h[i, i] += 2.0 * (1.0 + np.sin(3.0 * pg * x[ip])**2)
        h[i, i] *= cost

        h[i, ip] = 12.0 * pg * (x[i] - 1.0) * np.sin(3.0 * pg * x[ip]) * np.cos(3.0 * pg * x[ip])
        h[i, ip] *= cost

        h[ip, i] = h[i, ip]

    h[-1, -1] = 18.0 * pg**2 * (x[nm - 1] - 1.0)**2 * (np.cos(3.0 * pg * x[-1])**2 - np.sin(3.0 * pg * x[-1])**2)
    h[-1, -1] += 2.0 * (1.0 + np.sin(2.0 * pg * x[-1])**2)
    h[-1, -1] += 8.0 * (x[-1] - 1.0) * np.sin(2.0 * pg * x[-1]) * np.cos(2.0 * pg * x[-1]) * pg
    h[-1, -1] += 8.0 * (x[-1] - 1.0) * np.sin(2.0 * pg * x[-1]) * np.cos(2.0 * pg * x[-1]) * pg
    h[-1, -1] += 8.0 * pg**2 * (x[-1] - 1.0)**2 * (np.cos(2.0 * pg * x[-1])**2 - np.sin(2.0 * pg * x[-1])**2)
    h[-1, -1] *= cost

    return h

def zirilli14_hessian_direction(x, d):
    pg = np.arccos(-1.0)
    nm = len(x) - 1

    hd = np.zeros_like(x)

    c1 = 2.0 + 1200.0 * x[0]**2 - 400.0 * x[1]
    c2 = -400.0 * x[0]
    hd[0] = c1 * d[0] + c2 * d[1]

    for i in range(1, nm):
        ip = i + 1
        c1 = 202.0 + 1200.0 * x[i]**2 - 400.0 * x[ip]
        c2 = -400.0 * x[i]
        hd[i] = c1 * d[i] + c2 * d[ip]
        hd[ip] = c2 * d[i]

    hd[-1] = 200.0 * d[-1]

    return hd

if __name__ == "__main__":
    # Example usage
    n_dim = 3
    x_example = np.zeros(n_dim)

    function_value = zirilli14_function(x_example)
    gradient_value = zirilli14_gradient(x_example)
    hessian_value = zirilli14_hessian(x_example)
    hessian_direction_value = zirilli14_hessian_direction(x_example, gradient_value)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
    print("Hessian value:\n", hessian_value)
    print("Hessian x Direction value:", hessian_direction_value)
