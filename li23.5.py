#水平组合数组，行数必须得一样
#通过hstack函数可以将两个或者多个数组水平组合起来形成一个数组


#通过reshape方法以及乘法运算创建了3个二维数组（行数相同），然后使用hstack函数水平组合其中的两个或者三个数组

from numpy import *
a=arange(9).reshape(3,3)
b=a*3
print(a)
print(b)
c=a*5

#水平组合a和b
print(hstack((a,b)))  #注意：hstack后面有两个圆括号，别忘了！

#水平组合a和b,c
print(hstack((a,b,c)))