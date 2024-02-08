# power sum function
# 0 <= x <= n
# fstar = 0
#--------------------
#     POWER SUM FUNCTION
#--------------------


# TO TEST not known if it works

def funct(n, x):
    b = [8.0, 18.0, 44.0, 114.0]
    f = 0.0

    for k in range(1, n + 1):
        s = 0.0
        for j in range(1, n + 1):
            s += x[j - 1] ** k
        f += (s - b[k - 1]) ** 2

    return f


def grad(n, x):
    b = [8.0, 18.0, 44.0, 114.0]
    g = [0.0] * n

    s1 = sum(x)
    for i in range(1, n + 1):
        g[i - 1] = 2.0 * (s1 - b[0])
        for k in range(2, n + 1):
            s = 0.0
            for j in range(1, n + 1):
                s += x[j - 1] ** k
            g[i - 1] += 2.0 * (s - b[k - 1]) * k * x[i - 1] ** (k - 1)

    return g

if __name__ == "__main__":
    # Example Usage
    n_value = 4
    x_values = [1.0, 2.0, 3.0, 4.0]  # Replace with your actual input values

    result_funct = funct(n_value, x_values)
    result_grad = grad(n_value, x_values)

    print("Result (Function):", result_funct)
    print("Result (Gradient):", result_grad)
