import numpy as np

a = np.array([1, 2, 3], [1, 2]) 

print(a.ndim) #Number of dimensions of the array
print(a.shape) #Dimensions of the array
print(a.dtype) #Data type of the array
print(a.size) #Number of bits in the array
print(a.itemsize) #Size of each element in the array

print(a[1,1]) #Accessing an element in the array
print(a[1, :]) #Accessing a row in the array
print(a[:, 1]) #Accessing a column in the array
print(a[1, 1:3]) #Accessing a range of elements in the array
print(a[1, 1:3:2]) #Accessing a range of elements in the array with a step


zero = np.zeros((2, 3)) #Creating an array of zeros with shape (2, 3)
one = np.ones((4,2,2), dtype="int32") #Creating an array of ones with shape (4, 2, 2) and data type int32
five = np.full((2, 3), 5) #Creating an array filled with the value 5 with shape (2, 3)
identity = np.identity(3) #Creating a 3x3 identity matrix
similar = np.full_like(a, 5) # np.full(a.shape, 5)
random = np.random.rand(2, 3) #Creating an array of random values with shape (2, 3)
randomInt= np.random.randint(4, 7, size=(3,3)) #Creating an array of random integers between 4 and 7 with shape (3, 3)

arr = np.array([1, 2, 3])
r1 =np.repeat(arr, 3) #Repeating each element of the array 3 times
print(r1)

output = np.ones((5,5)) 
z = np.zeros((3,3))
z[1, 1] = 9 
output[1:4, 1:4] = z 
print(output)

a = np.array([1, 2, 3])
b = a.copy()  # Create a copy of the array
b[0] = 10  # Modify the copy

np.sin(a)  # Apply the sine function to the original array

#Linear algebra
x = np.ones((2, 3))
y = np.full((3, 2), 2)
z = np.matmul(x, y)  # Matrix multiplication of x and y
z2 = x.dot(y)  # Another way to perform matrix multiplication
np.linalg.det(z)  # Determinant of matrix z
np.linalg.inv(z)  # Inverse of matrix z

#Statistics
stats = np.array([[1, 2, 3], [4, 5, 6]])
np.min(stats)  # Minimum value in the array
np.max(stats, axis=0)  # Maximum value along columns    
np.max(stats, axis=1)  # Maximum value along rows
np.sum(stats, axis=0)  # Sum of each column

#Reshaping
before = np.array([[1, 2, 3], [4, 5, 6]])
after = before.reshape((3, 2))  # Reshape the array to shape (

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
np.vstack((v1, v2, v1, v2))  # Stack arrays vertically
np.hstack((v1, v2, v1, v2))  # Stack arrays horizontally

#File operations
filedata = np.loadtxt("data.txt")  # Load data from a text file
filedata = filedata.astype("int32")  # Change the data type to int32
print(filedata)

filedata > 50 # Create a boolean array where each element is True if the corresponding element in filedata is greater than 50
filedata[filedata > 50]  # Filter the array to get values greater than 50

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a[[1, 2, 8]] # Access specific elements in the array using indices
np.any(filedata > 50)  # Check if any element in filedata is greater than 50
(~((filedata > 50) & (filedata < 100)))  # Invert the boolean array where elements are True if they are not between 50 and 100






