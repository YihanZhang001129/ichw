# 通用的高速缓存存储器结构及工作原理

*结构*

一个通用的高速缓存存储器会有S = 2 ^ s个set（组）

每个set含有E个line（cache line），每个line又包含1位vaild bit、t位tag、B=2^b bytes cache block（存储数据的地方）。

若存储器地址有m位（cache block），则共有M = 2^m个不同的地址。

cache缓存数据的大小C=组的大小*组的数目=位的大小*每组行数*组的数目=B*E*S

内存大小为2^m；Cache line为大小2^b；内存的cache line个数为2^(m-b)。

2^(m-b)个cache line分到2^s个set里，每个set有2^(m-b–s)个cache line，即需（m-b-s）位tag标记出当前是哪个cache。也就是说t=m-b-s。 

