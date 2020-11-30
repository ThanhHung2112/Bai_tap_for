import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[2,3,4],[1,2,4]])
print('a = ',a)
print('b = ',b)
c=a+b
d=a*b
print('a+b = \n',c)
print('a*b = \n',d)
def chuyen_vi(mt) :
    kq= print(mt.transpose())
    return kq