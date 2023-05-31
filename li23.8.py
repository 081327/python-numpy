#垂直分隔数组
#使用vsplit函数
#使用vsplit函数将一个4*2的二维数组分隔成4个1*2数组

from numpy import *
a=arange(8).reshape(4,2)
#将4*2的二维数组分隔成4个1*2的数组
c=vsplit(a,4)
print(c)
print(c[0].shape)
print(c[0])
print(c[2])
