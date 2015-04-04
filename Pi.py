__author__ = 'Ingoo'
def pi(xList, xbar):
    pi = 1
    for x in xList:
        pi *= xbar - x
    return pi