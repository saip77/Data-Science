# What is Numpy?
'''
Numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and 
matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
'''

# Why not to use Python lists?
'''
Slow for math
Not memory efficient
Don't support vectorized operations
'''

#Importing Numpy
import numpy as np

#Check the version of Numpy
print(f'Numpy version: {np.__version__}')
 

#Creating a Numpy array
a = np.array([[1,2,3,4],[5,6,7,8]], dtype= int)
print(a)
 

#Special arrays
print(np.zeros((2,2)))    #2D array of zeros
 
print(np.ones((3,4,5)))   #3D array of ones
 
print(np.eye(3))          #Identity matrix
 

#Range functions
print(np.arange(0, 10, 2, dtype=int))             #Sequence of numbers from 0 to 8 with step 2 
print((np.linspace(0, 20, 5) * 10).astype(int))   #Sequence of numbers from 0 to 10 with 5 elements
 

#Array properties
newArr = np.array([[1,2,3,4,5],[6,7,8,9,10], [11,12,13,14,15]])
print(f'Shape i.e. number of rows and columns: {newArr.shape}')
print(f'Size i.e. total number of elements: {newArr.size}')
print(f'Number of dimensions: {newArr.ndim}')
 

#Indexing and Slicing
print(newArr[0])        #Returns the first row
 
print(newArr[1][1])     #Returns the second element of the second row
 
print(newArr[1:2])      #Start index is 1, end index is 2 (exclusive)
 
print(newArr[1:3:1])    #Start index is 1, end index is 3 (exclusive), step is 1
 
print(newArr[0,1])      #Returns the second element of the first row
 
print(newArr[0,:])      #Returns the first row, : means all columns
 
print(newArr[:,1])      #Returns the second column, : means all rows
 

#Mathematical operations
d = np.array([[1,2,3,4],[5,6,7,8]])
c = np.array([[20,30,40,50],[60,70,80,90]])
print(c + d)                         #Add two arrays
 
print(c * d)                         #Multiply two arrays
 
print(c - d)                         #Subtract two arrays
 
print((c / d).astype(int))           #Divide two arrays
 

#Broadcasting
c = c+10
print('After adding')
print(c)                             #Add 10 to each element
 

#Random Module
print(np.floor(np.random.rand(2,2)*10).astype(int))            #Generates a 2x2 array of random numbers
  
print(np.random.randint(0,10,3))                               #Generates a 3-element array of random integers between 0 and 10
 
print(np.floor(np.abs((np.random.randn(2,2)*10).astype(int)))) #Generates a 2x2 array of random numbers with a normal distribution
 
print(np.random.seed(42))

#Aggregation functions
e = np.array([[1,2,3,4],[5,6,7,8]])
print(e.sum())                      #Sum of all elements
 
print(e.mean())                     #Mean of all elements
 
print(e.min())                      #Minimum of all elements
 
print(e.max())                      #Maximum of all elements

#Axis
print(e.sum(axis=0))                #Sum of all elements along the first axis (column-wise)
 
print(e.sum(axis=1))                #Sum of all elements along the second axis (row-wise)

#Transpose and Determinant
f = np.array([[1,2,3],[4,5,6]])
g = f.T                             #Transpose i.e. switch rows and columns
print(g) 
detMatrix = np.array([[1,2],[3,4]])
h = int(np.linalg.det(detMatrix))   #Determinant of a matrix    
print(h)

#Sorting
i = np.array([[3,1,5],
              [6,4,2]])
j = np.sort(i, axis=0)  # sort along rows of each column
print(j)