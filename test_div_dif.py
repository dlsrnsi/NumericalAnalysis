__author__ = 'Ingoo'

from divided_difference import div_dif

xList = [1,1.5,2,3,3.5,4]
fxList = [0,0.4055,0.6931,1.0986,1.2528,1.3863]
x = 1.75
div_dif(xList,fxList,x)
x = 2.5
div_dif(xList,fxList,x)
x = 3.4
div_dif(xList,fxList,x)

'''

result : 0.5599558593750001

result : 0.9156000000000001

result : 1.2239369472

'''