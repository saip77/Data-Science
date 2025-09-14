import numpy as np
### print(np.__version__)

x = [1, 2, 3, 4, 5]
print(type(x))

### Converting a list to a numpy array

arr = np.array(x)
print(arr)
print(type(arr))

print(np.arange(10, 16))
print(np.arange(10, 16, 2))     # step size is 2
print(np.arange(10, 16, 0.5))   # step size is 0.5

### Print zeroes

print(np.zeros(5))


### 2-D Array

print(np.zeros((5, 5)))        # 5 rows and 5 columns
print(np.zeros((5, 5), dtype=int))  # 5 rows and 5 columns
print(np.ones((5, 5)))         # 5 rows and 5 columns
print(np.ones((5, 5), dtype=int))   # 5 rows and 5 columns



### Generating a random array
arr1 = np.random.randint(0, 10, 6)
print(arr1)

### Reshaping an array
print(arr1.reshape(2, 3))
