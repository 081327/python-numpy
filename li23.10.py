#存取numpy函数
#savetxt函数可以将numpy数组以指定的格式保存为文本文件，loadtxt函数能从文本文件中读取数据，并以numpy数组形式返回
from numpy import *
a=arange(20)
print(a)

#将数组a以整数格式保存成a.txt文件
savetxt("a.txt",a,fmt='%d')
#将数组a以浮点数格式保存成b.txt文件
savetxt("b.txt",a,fmt='%.2f')
#从a.txt文件以整数形式读取文本数据，并返回numpy数组
aa=loadtxt("a.txt",dtype='int')
#从b.txt文件以浮点数形式读取文本数据，并返回numpy数组
bb=loadtxt("b.txt",dtype='float')
print(aa)
print(bb)
