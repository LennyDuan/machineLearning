import scipy as sp

def error(f, x, y):
    print("Calculating the vector difference")
    return sp.sum((f(x) - y) ** 2)
