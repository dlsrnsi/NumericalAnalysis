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
    print("result", x)
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
    print("result", x)

def gauss_seidel(mat, b, TOL=0.00000001):#Matrix와 b를 참조변수로 받음
    mat = np.array(mat, dtype='float')
    b = np.array(b, dtype='float')
    print(mat)
    print(b)
    #계산하기 쉽게 바꿔줌
    x = [1] * np.shape(b)[0] # b의 길이만큼 1의 리스트를 만듬
    while True:
        for i in range(np.shape(mat)[0]): #행렬의 행의 길이만큼 해를 구함
            sum = 0
            for j in range(np.shape(mat)[0]):
                if i is j:
                    pass # i=j 일때는 계산 안함
                else:
                    sum -= mat[i, j] * x[j] #old와 new의 구분이 딱히 필요 없음
            sum = (sum + b[i])/mat[i, i]
            if np.abs(sum - x[i]) < TOL: #old와 new값이 TOL보다 작으면 정지
                print(x)
                return x
            else : x[i] = sum


