#加权平均数
#average函数求平均值
from numpy import *
price,weights=loadtxt('data.csv',delimiter=',',usecols=(6,7),unpack=True)
print(price)
print(weights)
#计算成交量加权平均价格
vwap=average(price,weights=weights)
print('vwap','=',vwap)