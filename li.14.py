#数组的中位数和方差
#median计算数组的中位数
#var计算数组的方差

from numpy import *

#计算元素个数为偶数的数组的中位数
a=array([4,2,1,5])
print(median(a))

#计算元素个数为奇数的数组的中位数
a=array([4,2,1])
print(median(a))

price=loadtxt('data.csv',delimiter=',',usecols=(6,),unpack=True)
print(price)
print(median(price))
print('方差：',var(price))