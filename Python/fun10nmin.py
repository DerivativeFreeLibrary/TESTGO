#*************************************************
#	FUNZIONE LEVY 8
#*************************************************
import numpy as np

def levy8_function(x):
    pg = np.arccos(-1.0)
    rk = 10.0
    ra = 1.0
    nm = len(x) - 1

    f = rk * np.sin(pg * x[0])**2

    for i in range(nm):
        ip = i + 1
        f += (x[i] - ra)**2 * (1.0 + rk * np.sin(pg * x[ip])**2)

    f += (x[-1] - ra)**2
    f *= pg / len(x)

    return f

def levy8_gradient(x):
    pg = np.arccos(-1.0)
    rk = 10.0
    ra = 1.0
    nm = len(x) - 1

    g = np.zeros_like(x)

    g[0] = 2.0 * pg * rk * np.sin(pg * x[0]) * np.cos(pg * x[0])
    g[0] += 2.0 * (x[0] - ra) * (1.0 + rk * np.sin(pg * x[1])**2)
    g[0] *= pg / len(x)

    for i in range(1, nm):
        im = i - 1
        ip = i + 1

        g[i] = 2.0 * rk * pg * (x[im] - ra)**2 * np.sin(pg * x[i]) * np.cos(pg * x[i])
        g[i] += 2.0 * (x[i] - ra) * (1.0 + rk * np.sin(pg * x[ip])**2)
        g[i] *= pg / len(x)

    g[-1] = 2.0 * rk * pg * (x[-2] - ra)**2 * np.sin(pg * x[-1]) * np.cos(pg * x[-1])
    g[-1] += 2.0 * (x[-1] - ra)
    g[-1] *= pg / len(x)

    return g

def levy8_hessian(x):
    pg = np.arccos(-1.0)
    rk = 10.0
    ra = 1.0
    nm = len(x) - 1

    h = np.zeros((len(x), len(x)))

    h[0, 0] = 2.0 * rk * pg**2 * (np.cos(pg * x[0])**2 - np.sin(pg * x[0])**2)
    h[0, 0] += 2.0 * (1.0 + rk * np.sin(pg * x[1])**2)
    h[0, 0] *= pg / len(x)

    h[0, 1] = 4.0 * rk * pg * (x[0] - ra) * np.sin(pg * x[1]) * np.cos(pg * x[1])
    h[0, 1] *= pg / len(x)
    h[1, 0] = h[0, 1]

    for i in range(1, nm):
        ip = i + 1
        im = i - 1

        h[i, i] = 2.0 * rk * pg**2 * (x[im] - ra)**2 * (np.cos(pg * x[i])**2 - np.sin(pg * x[i])**2)
        h[i, i] += 2.0 * (1.0 + rk * np.sin(pg * x[ip])**2)
        h[i, i] *= pg / len(x)

        h[i, ip] = 4.0 * rk * pg * (x[i] - ra) * np.sin(pg * x[ip]) * np.cos(pg * x[ip])
        h[i, ip] *= pg / len(x)
        h[ip, i] = h[i, ip]

    h[-1, -1] = 2.0 * rk * pg**2 * (x[-2] - ra)**2 * (np.cos(pg * x[-1])**2 - np.sin(pg * x[-1])**2) + 2.0
    h[-1, -1] *= pg / len(x)

    return h

def levy8_hessian_direction(x, d):
    pg = np.arccos(-1.0)
    rk = 10.0
    ra = 1.0
    nm = len(x) - 1

    hd = np.zeros_like(x)

    hd[0] = 2.0 + 1200.0 * x[0]**2 - 400.0 * x[1]
    hd[1] = -400.0 * x[0]

    hd[0] += hd[0] + 2.0 * pg * (x[0] + 1.42513) * d[0] + (-400.0 * x[0]) * d[1]
    hd[1] += -400.0 * x[0] * d[0] + 202.0 + 1200.0 * x[1]**2 - 400.0 * x[2] * d[1]
    hd[-1] += 200.0 * d[-1]

    for i in range(2, nm):
        ip = i + 1
        hd[i] += 202.0 + 1200.0 * x[i-1]**2 - 400.0 * x[ip] * d[i] + (-400.0 * x[i-1]) * d[i-1]
        hd[ip] += -400.0 * x[i-1] * d[i] + (-400.0 * x[ip]) * d[i-1]

    hd[-1] += 200.0 * d[-1]

    return hd

if __name__ == "__main__":
    # Example Usage
    n_value = 3
    x_values = np.array([1.0, 2.0, 3.0])  # Replace with your actual input values

    result_funct = levy8_function(x_values)
    result_grad = levy8_gradient(x_values)
    result_hess = levy8_hessian(x_values)
    result_hess_dir = levy8_hessian_direction(x_values, np.ones_like(x_values))

    print("Result (Function):", result_funct)
    print("Result (Gradient):", result_grad)
    print("Result (Hessian):", result_hess)
    print("Result (Hessian Direction):", result_hess_dir)
