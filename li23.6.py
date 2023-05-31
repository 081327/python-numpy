#垂直数组组合，列数必须得一样
#使用vstack函数将两个或多个数组垂直组合起来形成一个数组

from numpy import *
a=arange(12).reshape(3,4)
b=arange(16).reshape(4,4)
c=arange(20).reshape(5,4)
print(a)
print(b)
print(c)
print(vstack((a,b,c)))