m = int(input())
n = int(input())
a = int(input())
b = int(input()) 
qiang = [0]*(m*n)
result = []

def check(i,j,a,b):                    ###检验从第i行第j列能否铺砖
	for idx in range(i,i+a):
		for jdx in range(j,j+b):
			if idx >= m or jdx >= n:   ###越界错误
				
				return False

			elif qiang[n * idx + jdx] == 1:
				return False           ###铺过错误

	return True

def puchai(ans,i,j,a,b,v):
	'''
	从（i,j）开始铺砖，v为1铺，为0拆
	'''
	tmp = []                           ###尝试样本
	for idx in range(i,i + a):
		for jdx in range(j,j + b):
			v = qiang[n * idx + jdx]
			tmp.append(n * idx + jdx)

	if v == 1:
		ans.append(tmp)
	else:
		ans.remove(tmp)


def puzhuan(ans,i,j):
	'''
	从第i行第j列开铺
	'''
	if i == m-1 and j == n:
		###最后一个位置
		print(ans)
		result.append(ans.copy())
	elif j == n:
		puzhuan(ans,i+1,0)###换下一行最开始
		return
	if qiang[n*i+j] == 1:
		puzhuan(ans,i,j+1)###铺下一块
		return
	if check(i,j,a,b):###检验能否横铺
		puchai(ans,i,j,a,b,1)###铺上去
		puzhuan(ans,i,j+b)###铺下一块砖
		puchai(ans,i,j,a,b,0)###拆下来
	if a != b and check(i,j,b,a):###检验能否竖铺
		puchai(ans,i,j,b,a,1)
		puzhuan(ans,i,j+a)
		puchai(ans,i,j,b,a,0)

	return

puzhuan([],0,0)
print(len(result))

##这是对照助教代码写的，只能写到这里了。##
##以下为原始代码：##

result = []
m = int(input())
n = int(input())
a = int(input())
b = int(input())    
qiang = [[0]*n]*m    
    
###*****************************************************小函数

###求编号
def bianhao(i,j,m,n):
    return (j-1)+n*(i-1)
    
####判断墙是否满
def ifpuman(qiang):
    for i in qiang:
        o = 0
        z = 0
        while z < len(qiang):
            z = z + 1
            if 0 not in i:
                o = o + 1
        if o == len(qiang):
            return '铺满了'
        else:
            return '没有满'

###判断能否横铺
def ifheng(qiang,i,j,a,b):
    for k in range(i,i+a+1):
        if 1 not in qiang[k][j:j+b+1]:
            return '能横铺'
        else:
            return '不能横铺'
        
###判断能否竖铺
def ifshu(qiang,i,j,a,b):
    for k in range(i,i+b+1):
        if 1 not in qiang[k][j:j+a+1]:
            return '能竖铺'
        else:
            return '不能竖铺'        
    
#####************************************************************小函数结束
  
def puzhuan(qiang):
    
    
    
    if ifpuman(qiang) == '铺满了':
        return result
    else:
        for i in qiang:
            for j in i:
                if int(j) == 0:
                    
                    if ifheng(qiang,i,j,a,b) == '能横铺':
                        
                        for k in range(i,i+a+1):
                            for l in qiang[k][j:j+b+1]:
                                l = 1
                                result.append(bianhao(ord(k),ord(l),m,n))           
                        puzhuan(qiang)
                        
                       
                        for k in range(i,i+a+1):    ###remove
                            for l in qiang[k][i:j+b+1]:
                                l = 0
                                result.pop(bianhao(ord(k),ord(l),m,n))
                        
                    if ifshu(qiang,i,j,a,b) == '能竖铺':
                        
                        for k in range(i,i+b+1):
                            for l in qiang[k][j:j+a+1]:
                                l = 1
                                result.append(biaohao(ord(k),ord(l),m,n))
                        puzhuan(qiang)
                        
                      
                        for k in range(i,i+b+1):    ###remove
                            for l in qiang[k][i:j+a+1]:
                                l = 0
                                result.pop(bianhao(ord(k),ord(l),m,n))
                                
                    return result
                        
                    
                    
                        
print(puzhuan(qiang))                  
    


result = []
m = int(input())
n = int(input())
a = int(input())
b = int(input())    
qiang = [[0]*n]*m    
    
###*****************************************************小函数

###求编号
def bianhao(i,j,m,n):
    return (j-1)+n*(i-1)
    
####判断墙是否满
def ifpuman(qiang):
    for i in qiang:
        o = 0
        z = 0
        while z < len(qiang):
            z = z + 1
            if 0 not in i:
                o = o + 1
        if o == len(qiang):
            return '铺满了'
        else:
            return '没有满'

###判断能否横铺
def ifheng(qiang,i,j,a,b):
    for k in range(i,i+a+1):
        if 1 not in qiang[k][j:j+b+1]:
            return '能横铺'
        else:
            return '不能横铺'
        
###判断能否竖铺
def ifshu(qiang,i,j,a,b):
    for k in range(i,i+b+1):
        if 1 not in qiang[k][j:j+a+1]:
            return '能竖铺'
        else:
            return '不能竖铺'        
    
#####************************************************************小函数结束
  
def puzhuan(qiang):
    
    
    
    if ifpuman(qiang) == '铺满了':
        return result
    else:
        for i in qiang:
            for j in i:
                if int(j) == 0:
                    
                    if ifheng(qiang,i,j,a,b) == '能横铺':
                        
                        for k in range(i,i+a+1):
                            for l in qiang[k][j:j+b+1]:
                                l = 1
                                result.append(bianhao(ord(k),ord(l),m,n))           
                        puzhuan(qiang)
                        
                       
                        for k in range(i,i+a+1):    ###remove
                            for l in qiang[k][i:j+b+1]:
                                l = 0
                                result.pop(bianhao(ord(k),ord(l),m,n))
                        
                    if ifshu(qiang,i,j,a,b) == '能竖铺':
                        
                        for k in range(i,i+b+1):
                            for l in qiang[k][j:j+a+1]:
                                l = 1
                                result.append(biaohao(ord(k),ord(l),m,n))
                        puzhuan(qiang)
                        
                      
                        for k in range(i,i+b+1):    ###remove
                            for l in qiang[k][i:j+a+1]:
                                l = 0
                                result.pop(bianhao(ord(k),ord(l),m,n))
                                
                    return result
                        
                    
                    
                        
print(puzhuan(qiang))                  
    
    
    拖了这么久也没有拖出个结果。


