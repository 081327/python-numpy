#创建多维数组,array函数可以生成多维数组
#shape表示可以获取数组每一维度的元素个数，也可以通过shape[n]形式获得每一维的元素个数
from numpy import *
a=arange(5)
print(a)

#输出数组每一个维度的元素个数
print(a.shape)

#输出第一维的元素个数
print(a.shape[0])

#创建一个3*3的二维数组
m1=array([arange(3),arange(3),arange(3)])   #注意：里面要用[],而且里面用数组形式的arange函数
print(m1)


#创建一个2*3的二维数组
m2=array([arange(3),arange(3)])
print(m2)


#创建一个3*3的混合类型的数组（每个元素的类型可能不一样）
m3=array([["a","b",4],[1,2,3],[5.3,5,3]])
print(m3)


#这块是中重点！！！
#输出m2数组每一个维度元素的个数，运行结果为（2，3）
print(m2.shape)


##运行结果：m2是二维数组
print("{}是{}维数组".format("m2",len(m2.shape)))

#输出m2的第一维的元素个数，运行结果为2
print(m2.shape[0])

#输出m2的第二维的元素个数，运行结果为3
print(m2.shape[1])