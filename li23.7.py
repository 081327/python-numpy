#水平分隔数组
#使用hsplit函数，注意第二个参数必须可以整除待分隔数组的列数
from numpy import *
a=arange(8).reshape(2,4)
print(a)

#将2*4的二维数组分隔成4个2*1的二维数组，注意：运行结果的呈现！！！
b=hsplit(a,4)
print(b)
print(b[0],shape)
print(b[0])
print(b[2])
#将2*4的二维数组分隔成2个2*2的二维数组
print(hsplit(a,2))