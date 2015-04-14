__author__ = '200913215 이인구'
import numpy as np

def bisection(a, b, f, tol):
    while True:
        n = 0
        while n < 100:
            p = a + (b - a)/2
            if np.abs(f(p)) < tol:
                print("result :")
                print("a : ", a, " b : ", b)
                print("p : ", p, " f(p) : ", f(p))
                return a, b
            if f(a) * f(p) > 0:
                a = p
            else :
                b = p
            n += 1
        a = a + 1
        b = b - 1

def regular_falsi(a, b, f, tol):
    q0 = f(a)
    q1 = f(b)
    n =0
    while True:
        if np.abs(q1 - q0) < tol:
            raise ValueError("q1 - q0 is too small")
        p = b - q1 * ((b - a) / (q1 - q0))
        q = f(p)
        if np.abs(q) < tol:
            print("result :")
            print("a : ", a, " b : ", b)
            print("p : ", p, " f(p) : ", f(p))
            break
        if q1 * f(p) < 0:
            a = b
            q0 = q1
        b = p
        q1 = q

def secant(a, b, f, tol):
    q0 = f(a)
    q1 = f(b)
    while True:
        p = b - q1 * ((b - a) / (q1 - q0))
        if np.abs(f(p)) < tol:
            print("result :")
            print("a : ", a, " b : ", b)
            print("p : ", p, " f(p) : ", f(p))
            break
        a = b
        q0 = q1
        b = p
        q1 = f(p)

def newton_rapson(a,b,f,f_prime,tol):
    while True:
        p = b - f(a)/f_prime(a)
        if np.abs(f(p)) < tol:
            print("result :")
            print("a : ", a, " b : ", b)
            print("p : ", p, " f(p) : ", f(p))
            break
        a = p
