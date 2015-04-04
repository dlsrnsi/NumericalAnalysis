__author__ = 'Ingoo'
from equation import *
import numpy as np

equation = lambda x : (x**2)/4 - np.sin(x) + 0.1
equation_prime = lambda x : x/2 - np.cos(x)

bisection(-1,1,equation,0.000001)
regular_falsi(-1,1,equation,0.000001)
secant(-1,1,equation,0.000001)
newton_rapson(-1,0.5,equation,equation_prime,0.000001)

'''
result :
a :  0.10282135009765625  b :  0.1028289794921875
p :  0.10282516479492188  f(p) :  -8.11604427761e-07
result :
a :  -1  b :  0.102826428992
p :  0.102824573973  f(p) :  -2.54278458137e-07
result :
a :  0.105738370341  b :  0.102791307832
p :  0.102824335204  f(p) :  -2.90460384217e-08
result :
a :  2.3331124863  b :  0.5
p :  0.10282519141  f(p) :  -8.36710539118e-07
'''