#*************************************************
#	FUNZIONE LEVY 5
#*************************************************

import numpy as np

def levy5_function(x):
    pg = np.arccos(-1.0)
    ct = 25.0e-2
    rk = 10.0
    ra = 1.0
    nm = len(x) - 1

    f = rk * np.sin(pg * (1.0 + ct * (x[0] - 1.0)))**2

    for i in range(nm):
        ip = i + 1
        f += (((1.0 + ct * (x[i] - 1.0)) - ra)**2) * (1.0 + rk * np.sin(pg * (1.0 + ct * (x[ip] - 1.0)))**2)

    f += ((1.0 + ct * (x[-1] - 1.0)) - ra)**2
    f *= (pg / nm) * ct

    return f

def levy5_gradient(x):
    pg = np.arccos(-1.0)
    ct = 25.0e-2
    rk = 10.0
    ra = 1.0
    nm = len(x) - 1

    g = np.zeros_like(x)

    g[0] = 2.0 * pg * rk * np.sin(pg * (1.0 + ct * (x[0] - 1.0))) * np.cos(pg * (1.0 + ct * (x[0] - 1.0)))
    g[0] += 2.0 * ((1.0 + ct * (x[0] - 1.0)) - ra) * (1.0 + rk * np.sin(pg * (1.0 + ct * (x[1] - 1.0)))**2)
    g[0] *= (pg / nm) * ct

    for i in range(1, nm):
        im = i - 1
        ip = i + 1

        g[i] = 2.0 * rk * pg * (((1.0 + ct * (x[im] - 1.0)) - ra)**2) * np.sin(pg * (1.0 + ct * (x[i] - 1.0))) * np.cos(pg * (1.0 + ct * (x[i] - 1.0)))
        g[i] += 2.0 * ((1.0 + ct * (x[i] - 1.0)) - ra) * (1.0 + rk * np.sin(pg * (1.0 + ct * (x[ip] - 1.0)))**2)
        g[i] *= (pg / nm) * ct

    g[-1] = 2.0 * rk * pg * (((1.0 + ct * (x[nm - 1] - 1.0)) - ra)**2) * np.sin(pg * (1.0 + ct * (x[-1] - 1.0))) * np.cos(pg * (1.0 + ct * (x[-1] - 1.0)))
    g[-1] += 2.0 * ((1.0 + ct * (x[-1] - 1.0)) - ra)
    g[-1] *= (pg / nm) * ct

    return g

def levy5_hessian(x):
    pg = np.arccos(-1.0)
    ct = 25.0e-2
    rk = 10.0
    ra = 1.0
    nm = len(x) - 1

    h = np.zeros((len(x), len(x)))

    h[0, 0] = 2.0 * rk * (pg**2) * (np.cos(pg * (1.0 + ct * (x[0] - 1.0)))**2 - np.sin(pg * (1.0 + ct * (x[0] - 1.0)))**2)
    h[0, 0] += 2.0 * (1.0 + rk * np.sin(pg * (1.0 + ct * (x[1] - 1.0)))**2)
    h[0, 0] *= (pg / nm) * ct**2

    h[0, 1] = 4.0 * rk * pg * ((1.0 + ct * (x[0] - 1.0)) - ra) * np.sin(pg * (1.0 + ct * (x[1] - 1.0))) * np.cos(pg * (1.0 + ct * (x[1] - 1.0)))
    h[0, 1] *= (pg / nm) * ct**2

    h[1, 0] = h[0, 1]

    for i in range(1, nm):
        ip = i + 1
        im = i - 1

        h[i, i] = 2.0 * rk * (pg**2) * (((1.0 + ct * (x[im] - 1.0)) - ra)**2) * (np.cos(pg * (1.0 + ct * (x[i] - 1.0)))**2 - np.sin(pg * (1.0 + ct * (x[i] - 1.0)))**2)
        h[i, i] += 2.0 * (1.0 + rk * np.sin(pg * (1.0 + ct * (x[ip] - 1.0)))**2)
        h[i, i] *= (pg / nm) * ct**2

        h[i, ip] = 4.0 * rk * pg * ((1.0 + ct * (x[i] - 1.0)) - ra) * np.sin(pg * (1.0 + ct * (x[ip] - 1.0))) * np.cos(pg * (1.0 + ct * (x[ip] - 1.0)))
        h[i, ip] *= (pg / nm) * ct**2

        h[ip, i] = h[i, ip]

    h[-1, -1] = 2.0 * rk * (pg**2) * (((1.0 + ct * (x[nm - 1] - 1.0)) - ra)**2) * (np.cos(pg * (1.0 + ct * (x[-1] - 1.0)))**2 - np.sin(pg * (1.0 + ct * (x[-1] - 1.0)))**2)
    h[-1, -1] += 2.0 * (1.0 + rk * np.sin(pg * (1.0 + ct * (x[-1] - 1.0)))**2)
    h[-1, -1] *= (pg / nm) * ct**2

    return h

def levy5_hessian_direction(x, d):
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

    function_value = levy5_function(x_example)
    gradient_value = levy5_gradient(x_example)
    hessian_value = levy5_hessian(x_example)
    hessian_direction_value = levy5_hessian_direction(x_example, gradient_value)

    print("Function value:", function_value)
    print("Gradient value:", gradient_value)
    print("Hessian value:\n", hessian_value)
    print("Hessian x Direction value:", hessian_direction_value)
