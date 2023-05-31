#读写CSV文件
#csv文件是用分隔符分隔的文本文件，通常的分隔符包括空格，逗号，分号等，通过loadtxt函数可以读取csv文件，通过savetxt函数可以将数组保存成csv文件
#可以通过delimiter关键字参数指定分隔符，还可以通过usecols关键字参数将读取的数据拆成多列返回，列索引从0开始

from numpy import *
a=arange(20).reshape(4,5)
print(a)
#将二维数组保存到a.txt文件中，并用逗号分隔
savetxt('a.txt',a,fmt='%d',delimiter=',')
#从a.txt文件以整数类型装载数据，只获取第2，4，5列数据
b=loadtxt('a.txt',dtype=int,delimiter=',',usecols=(1,3,4))
print(b)
   
#获取第一列和第四列的数据，并分别将数据赋给x变量和y变量
#注意：分别返回多列，必须将unpack关键字参数的值设为True！！！
x,y=loadtxt('a.txt',dtype=int,delimiter=',',usecols=(1,4),unpack=True)
print(x)
print(y)