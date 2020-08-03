def MaoPaoSort(iters=None):
    """冒泡算法"""
    flag=False
    for i in range(len(iters)-1,0,-1):
        if flag==True:
            break
        flag=True
        for j in range(0,i):
            if iters[j]<iters[j+1]:
                iters[j],iters[j+1]=iters[j+1],iters[j]
                flag=False
    return iters

def MaoPaoSort1(iters):
    low,high=0,len(iters)-1
    while low<high:
        for i in range(0,high):
            """正向冒泡寻求最小值"""
            if iters[i]<iters[i+1]:
                iters[i],iters[i+1]=iters[i+1],iters[i]
        high-=1
        for j in range(high,low,-1):
            """反向冒泡寻求最大值"""
            if iters[j]>iters[j-1]:
                iters[j],iters[j-1]=iters[j-1],iters[j]
        low+=1
    return iters

def InsertSort(iters):
    """插入排序"""
    for i in range(1,len(iters)):
        temp=iters[i]
        j=i-1
        while j>=0 and iters[j]>temp:
            iters[j+1]=iters[j]
            j-=1
        iters[j+1]=temp
    return iters

def ShellSort(iters):
    """希尔排序"""
    space=len(iters)//2
    while space>=1:
        ShellInsert(iters,len(iters),space)
        space=space//2
    return iters
def ShellInsert(iters,length,space):
    for i in range(space,length):
        temp=iters[i]
        j=i-space
        while j>=0 and iters[j]>temp:
            iters[j+space]=iters[j]
            j=j-space
        iters[j+space]=temp
