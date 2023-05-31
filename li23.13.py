#数组的最大值，最小值和取值范围
#max、min、ptp函数

from numpy import *
h,l=loadtxt('data.csv',delimiter=',',usecols=(4,5),unpack=True)
print('highest','=',max(h))
print('lowest','=',min(l))
print('范围','=',max(h)-min(l))
#通过ptp函数计算取值范围，也就是最大与最小值之差
print('范围','=',ptp(h))