import numpy as np

# a = np.array([1, 2, 3])
# # print(a)
# # print(a.shape)
# # print(a.dtype)
# # print(a.ndim)
# # print(a.size)
# # print(a.itemsize)
# # for i in range(3):
# #     print(a[i])

# b = a * np.array([1, 2, 5])
# # print(b)

# # difference between np arrays and python lists
# my_list = [3, 5, 6]

# my_list.append(8)

# # b.append(4)  # wouldnot work
# print(a)
# print(my_list)
# my_list = my_list + [3]
# # this adds four to each element of the np array
# a = a + np.array([4])
# print(a)
# print(my_list)
# # multiplication
# a = a * 2
# my_list = my_list * 2
# print(a)
# print(my_list)

# # squares every element in np array
# a = np.sqrt(a)

# dot products using numpy
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]

# a1 = np.array(l1)
# a2 = np.array(l2)

# dot = np.dot(a1, a2)
# dot2 = a1 @ a2
# print(dot2)

# multidimensional arrays
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a.ndim)
# print(a.shape)
# print(a[0, 1])
# # print(a[:, 0])
# print(a.T)
# print(np.linalg.inv(a))
# print(np.linalg.det(a))
