#利用Numpy中的API对数组进行维度操作
#reshape函数能将一维数组变成多维数组
#ravel或flatten函数能将多维数组变成一维数组
#shape或者resize函数可以随意改变数组的维度
#transpose函数可以对数组进行转置




from numpy import *
#将一维数组变成三维数组
b=arange(24).reshape(2,3,4)
print(b)


#将三维数组变成一维数组
b1=b.ravel()
print(b1)

#将三维数组变成二维数组！！！注意！！！
b.shape=(6,4)
print(b)


#数组的转置
b3=b.transpose()
print(b3)




