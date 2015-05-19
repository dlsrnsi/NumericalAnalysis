import numpy as np
from linear_algebra import *

mat = [[2, -1, 0, 0],
       [-1, 2, -1, 0],
       [0, -1, 2, -1],
       [0, 0, -1, 2]]
b = [1, 2, 3, 4]
#thomas(mat,b)
mat = [[2, 3, -1],
       [4, 4, -3],
       [-2, 3 , -1]]
b = [5, 3, -1]
#gauss(mat, b)

mat = [[8, 2, 3],
       [1, -9, 2],
       [2, 3, 6]]
b = [30, 1, 31]
gauss_seidel(mat, b)