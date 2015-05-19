import numpy as np
from Numerical_Calculus import *

pi = np.pi
f = lambda x: np.sin(pi * x)
dif_f = lambda x: pi*np.cos(pi*x)
h = 0.1
x = 0.16
print("two_point")

for i in range(15):
    true_val = dif_f(x)
    app_val = two_point_differentiation(f, x, h)
    print("h : %1.16f app_val : %1.16f error: %1.16f" % (h, app_val, (true_val - app_val)))
    h = h/10.

print("three_point")
h = 0.1
for i in range(15):
    true_val = dif_f(x)
    app_val = three_point_differentiation(f, x, h)
    print("h : %1.16f app_val : %1.16f error: %1.16f" % (h, app_val, (true_val - app_val)))
    h = h/10.

f = lambda x : np.exp(x) - np.sin(np.pi * x)
dif_two_f = lambda x : np.exp(x) + np.power(np.pi,2) * np.sin(np.pi * x)
x = 1.5
true_val = dif_two_f(x)
val_01 = richardson(f, x, 0.1)
val_001 = richardson(f, x, 0.01)
print(("h : %1.16f app_val : %1.16f error: %1.16f" % (0.1, val_01, (true_val - val_01))))
print(("h : %1.16f app_val : %1.16f error: %1.16f" % (0.01, val_001, (true_val - val_001))))

f = lambda x : np.log(x) # 자연로그 함수 정의
area1 = trapezoid(f, 1, 2)
area2 = simpson(f, 1, 2)
print("trapezoid : ", area1)
print("simpson : ", area2)

f = lambda x : np.exp(x) + np.power(x, 2) + 1
n = 10
area1 = trapezoid_integral(f, 0, 1, n)
area2 = simpson_integral(f, 0, 1, n)
print("trapezoid_integral : ", area1)
print("simpson_integral : ", area2)