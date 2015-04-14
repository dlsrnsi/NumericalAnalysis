import numpy as np

def thomas(mat,b):
    mat = np.matrix(mat, dtype='float')
    b = np.array(b, dtype='float')
    size = np.shape(mat)[0]
    for i in range(1, size):
        mat[i,i] = mat[i, i] - (mat[i-1, i] * (mat[i, i-1] / mat[i-1, i-1]))
        b[i] = b[i] - b[i-1] * (mat[i, i-1] / mat[i - 1, i - 1])
    x = np.zeros(size)
    x[size - 1] = b[size - 1] / mat[size - 1, size -1]
    print(mat)
    print(b)
    for i in range(size - 2, -1, -1):
        x[i] = (b[i] - mat[i,i+1] * x[i + 1]) / mat[i, i]
    print(x)
    return x

def gauss(mat, b):

    b = np.array([b], dtype='float')
    mat = np.array(mat, dtype='float')
    size = np.shape(mat)[0]
    mat = np.concatenate((mat, b.T),axis=1)
    for i in range(size):
        pset = mat[i:, i]
        if min(pset) == 0 :
            raise ValueError("No unique solution exist")
        p = i + pset.argmin()
        print(p)
        if p is not i:
            tempmat = mat[p, :].copy()
            mat[p, :] = mat[i, :]
            mat[i, :] = tempmat
        for j in range(i+1, size):
            m = mat[j, i]/mat[i, i]
            mat[j, :] = mat[j, :] - m * mat[i, :]
    if mat[size-1, size-1] == 0:
        raise ValueError("No unique solution exist")
    x = np.zeros(size)
    x[size -1] = mat[size-1, size] / mat[size-1, size-1]
    for i in range(size-1, -1, -1):
        sum = 0
        for j in range(i+1, size):
            sum += mat[i,j] * x[j]
        x[i] = (mat[i, size] - sum) / mat[i, i]
    print(mat)
    print(x)
