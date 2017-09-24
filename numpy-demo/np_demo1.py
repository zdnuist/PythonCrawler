# pip3 intall numpy
import numpy as np

data = np.array([2,3,5,9,44])
print(data)

data1 = np.array([[3,5,2,44],np.arange(4)])
print(data1)
#查看数组的维度
print(data1.shape)
#查看数据格式
print(data1.dtype)

arr = np.array(np.arange(10))
print(arr * 2)

#矩阵乘法
a = np.array([[1,2],[1,1]])
b = np.array([[1,2],[1,2]])
print(a)
c = np.dot(a,b)
print("c:")
print(c)

print(arr[5:8])

#生存多维矩阵
a,b = np.meshgrid(np.arange(1,5),np.arange(2,4))
print(a)
print(b)

# np.where
arr1 = np.arange(5)
arr2 = np.arange(20,25)
condition = np.array([1,0,1,0,0])
result = np.where(condition,arr1,arr2)
print(arr1)
print(arr2)
print(result)

arr3 = np.random.randint(1,20,10)
print(arr3)