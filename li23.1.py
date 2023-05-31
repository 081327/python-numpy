#arange函数
#arange函数  可以传入一个整数类型的参数值，返回一个0到n-1数组类型
#使用arange函数生成了多个ndarray类型的数组，并对数组进行加和次方的运算
 

#导入numpy模块的arange函数
from numpy import arange
def sum(n):
    #对ndarray类型的数组进行2次方运算
    a=arange(n)**2
    #对数组进行4次方运算
    b=arange(n)**4
    #将两个ndarray数组相加（每个数组元素相加）
    c=a+b
    return c
print(arange(5))
print(arange(5)**2)
print(arange(5)**4)
print(sum(5))
