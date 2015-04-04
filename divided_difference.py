__author__ = 'Ingoo'

def div_dif(xList, fxList ,x,result =0,n=0):
    if len(xList) == n:
        print("")
        print("result :", result)
        return result
    elif n==0 :
        result +=fxList[0]
    n = n+1
    nextfxList =[]
    for y in range(len(fxList)-1):
        ak = (fxList[y+1] - fxList[y])/(xList[y+n] - xList[y])
        if y == 0 :
            pi = 1
            for  z in range(len(xList) - len(fxList) +1):
                pi *= (x - xList[z])
            result += ak*pi
        nextfxList.append(ak)
    return div_dif(xList,nextfxList,x,result,n)
