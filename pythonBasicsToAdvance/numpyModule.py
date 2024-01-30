import numpy as np

arr = np.array([[1,2,3,4,5] , [6,7,8,9,10]])
arr1 = np.array((1,2,3,4,5))
arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# print(type(arr))
# print(type(arr1))


# print(np.__version__)
# print(arr)


# print(arr.shape)

# newarr2 = arr2.reshape(4,3)
# print(newarr2)

x = np .where(arr  == 6)
print(x)
