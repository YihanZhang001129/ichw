# 通用的高速缓存存储器结构及工作原理

**结构**

一个通用的高速缓存存储器会有S = 2 ^ s个set（组）

每个set含有E个line（cache line），每个line又包含1位vaild bit、t位tag、B=2^b bytes cache block（存储数据的地方）。

若存储器地址有m位（cache block），则共有M = 2^m个不同的地址。

cache缓存数据的大小C=(组的大小) * (组的数目)=(位的大小) * (每组行数) * (组的数目)=B * E * S

内存大小为2^m；Cache line为大小2^b；内存的cache line个数为2^(m-b)。

2^(m-b)个cache line分到2^s个set里，每个set有2^(m-b–s)个cache line，即需（m-b-s）位tag标记出当前是哪个cache，即t=m-b-s。 

**原理**

高速缓存确定一个请求是否命中，然后抽取出被请求的字的过程，分为三步:1）组选择; 2）行匹配; 3）字抽取。

  **直接映射**

  直接映射每个组只有一行
  
  
  *选组*

地址中取s bits选组


  *选行*

地址中取t bits与cache line中t bits tag匹配，匹配则命中，不匹配则cache miss。


  *字抽取*

地址中的b bits就是cache line中偏移，在命中的cache line中的取字。直接映射不命中时，直接把索引的组中的cache line替换掉即可。

  **组相连映射**
  
  组相连映射中，一个组包括多个cache line。
  
  
 *选组*

组相连映射的组选择与直接映射一致。


 *选行*

cache line的选择时，一个set中有多个cache line，因此需要搜索set中的每个cache line的tag，对比检查是否命中。


 *字抽取*

与直接映射一致。

组相连映射对于一个index就会有多个行与之相对应，比较每行的tag是否与想要的地址相符合，这样就会大大增加命中的几率，避免了一小段程序中频繁cache失效的问题。

组相连映射不命中时，由于索引到的组中会有多个cache line，因此会有多种算法选择到底替换哪个cache line。


 **全相连映射**
 
 全相连映射就是组相连映射只有一个组的情况。


  *选组*

全相连映射只有一个组，不需要组索引，s = 0，地址只被划分为一个标记tag和一个偏移。


  *选行*

全相连映射cache line选择时，需要多缓存中的所有cache line进行搜索对比。


  *字抽取*

与之前一致。
