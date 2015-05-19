import numpy as np


def two_point_differentiation(f, x, h):
    dif_f = (-f(x - h) + f(x + h))/(2*h)
    return dif_f

def three_point_differentiation(f, x, h):
    dif_f = (-3*f(x) + 4*f(x + h) - f(x + 2*h))/(2*h)
    return dif_f


def richardson(f, x, h):
    dif_f =  (f(x - h) - 2*f(x) + f(x + h)) / np.power(h, 2)
    return dif_f


def trapezoid(f, a, b):
    area = (f(a) + f(b)) * (b - a) / 2
    return area


def simpson(f, a, b):
    h = (b - a) / 2
    area = h * (f(a) + 4*f(a + h) + f(b) ) / 3
    return area

def trapezoid_integral(f, a, b, n):
    h = (b - a) / n
    sum = (f(a) + f(b)) / 2
    for i in range(1, n):
        sum += f(a + i * h)
    sum *= h
    return sum


def simpson_integral(f, a, b, n):
    h = (b - a) / (2 * n)
    sum0 = f(a) + f(b)
    sum1 = 0
    sum2 = 0
    for i in range(1, 2 * n):
        if i % 2 is 0:
            sum2 += f(a + i * h)
        else:
            sum1 += f(a + i * h)
    sum = h * (sum0 + 4 * sum1 + 2 * sum2) / 3
    return sum