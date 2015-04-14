import numpy as np
from linear_algebra import *

mat = [[2, -1, 0, 0],
       [-1, 2, -1, 0],
       [0, -1, 2, -1],
       [0, 0, -1, 2]]
b = [1, 2, 3, 4]
thomas(mat,b)
mat = [[5, -1, 0],
       [-1, 5, -1],
       [-1, 0 , 5]]
b = [9, 4, -6]
gauss(mat, b)