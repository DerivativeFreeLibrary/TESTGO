#*************************************************
#	FUNZIONE SCHUBERT
#*************************************************
import numpy as np

def funct(x):
    f1 = np.sum([i * np.cos((i + 1) * x[0] + i) for i in range(1, 6)])
    f2 = np.sum([i * np.cos((i + 1) * x[1] + i) for i in range(1, 6)])
    result = f1 * f2 + (x[0] + 1.42513)**2 + (x[1] + 0.80032)**2
    return result

def grad(x):
    f1 = np.sum([i * np.cos((i + 1) * x[0] + i) for i in range(1, 6)])
    f2 = np.sum([i * np.cos((i + 1) * x[1] + i) for i in range(1, 6)])

    g1 = -np.sum([(i + 1) * i * np.sin((i + 1) * x[0] + i) for i in range(1, 6)]) * f2 + 2.0 * (x[0] + 1.42513)
    g2 = -np.sum([(i + 1) * i * np.sin((i + 1) * x[1] + i) for i in range(1, 6)]) * f1 + 2.0 * (x[1] + 0.80032)

    return np.array([g1, g2])

def hess(x):
    f1 = np.sum([i * np.cos((i + 1) * x[0] + i) for i in range(1, 6)])
    f2 = np.sum([i * np.cos((i + 1) * x[1] + i) for i in range(1, 6)])

    h = np.zeros((2, 2))

    for i in range(1, 6):
        h[0, 0] -= f2 * (i + 1)**2 * i * np.cos((i + 1) * x[0] + i)
        h[1, 1] -= f1 * (i + 1)**2 * i * np.cos((i + 1) * x[1] + i)

    h[0, 0] += 2.0
    h[1, 1] += 2.0

    f11 = np.sum([-i * (i + 1) * np.sin((i + 1) * x[0] + i) for i in range(1, 6)])
    f22 = np.sum([-i * (i + 1) * np.sin((i + 1) * x[1] + i) for i in range(1, 6)])

    h[0, 1] = f11 * f22
    h[1, 0] = h[0, 1]

    return h

def hesdir(x, d):
    nm = len(x) - 1
    hd = np.zeros(len(x))

    c1 = 2. + 1200. * x[0]**2 - 400. * x[1]
    c2 = -400. * x[0]
    hd[0] += c1 * d[0] + c2 * d[1]
    hd[1] += c2 * d[0]

    for i in range(2, nm + 1):
        ip = i + 1
        c1 = 202. + 1200. * x[i-1]**2 - 400. * x[ip-1]
        c2 = -400. * x[i-1]
        hd[i-1] += c1 * d[i-1] + c2 * d[i]
        hd[i] += c2 * d[i-1]

    hd[len(x)-1] += 200. * d[len(x)-1]

    return hd

if __name__ == "__main__":
    # Example Usage
    n_value = 2
    x_values = np.array([1.0, 2.0])  # Replace with your actual input values
    direction_values = np.array([0.5, 0.8])  # Replace with your actual direction values

    result_funct = funct(x_values)
    result_grad = grad(x_values)
    result_hess = hess(x_values)
    result_hesdir = hesdir(x_values, direction_values)

    print("Result (Function):", result_funct)
    print("Result (Gradient):", result_grad)
    print("Result (Hessian):", result_hess)
    print("Result (Hessian x Direction):", result_hesdir)
