__author__ = 'Ingoo'

def get_div_dif(xList, fxList , resultList = [],n=0):
    if len(xList) == n:
        return resultList
    n = n+1
    nextfxList = []
    for y in range(len(fxList)-1):
        result = (fxList[y+1] - fxList[y])/(xList[y+n] - xList[y])
        print('x%d -x%d : '%(y+n,y),result)
        resultList.append(result)
        nextfxList.append(result)
    return get_div_dif(xList,nextfxList,resultList,n)

def div_dif(xList, fxList,x):
    resultList = get_div_dif(xList,fxList)
    result = fxList[0]
    n = len(fxList)-1
    pointer = 0
    while True :
        if n == 0 :
            break
        else :
            pi = 1
            for y in range(len(fxList)-n):
                pi *= (x-xList[y])
            print("pi :",pi)
            print('result :' , resultList[pointer])
            result += pi*resultList[pointer]
            pointer += n
            n -= 1
    return result



xList = [1,1.5,2,3,3.5,4]
fxList = [0,0.4055,0.6931,1.0986,1.2528,1.3863]
x = 1.75


print(div_dif(xList,fxList,x))