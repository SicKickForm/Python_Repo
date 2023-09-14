import numpy

# Numpy module allows faster processing with array objects and math
# Array objects contain all the data in only one memory place (locality of reference)
# Array objects are called ndarray
# Numpy module methods
# Returns array object of specified array
print('0-D array')
print(numpy.array(1))
print('1-D array')
print(numpy.array([1, 2, 3, 4]))
print('2-D array')
print(numpy.array([[1, 2], [3, 4]]))
print('3-D array')
print(numpy.array([[[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']]]))
# Returns number of array object dimensions
print('ndim')
print(numpy.ndim([1, 2, 3, 4]))
# Specify number of array object dimensions
print('ndmin')
print(numpy.array([1, 2, 3, 4], ndmin=4))
# Array objects are also indexed
print('index')
print(numpy.array([[[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']]])[0, 0, 0])
print(numpy.array([[[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']]])[1, 1, -1])
# Array objects can also be sliced
print('slice')
print(numpy.array([1, 2, 3, 4])[0:4:2])
print(numpy.array([1, 2, 3, 4])[-3::2])
print(numpy.array([[[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']]])[1, 0:1])
print(numpy.array([[[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']]])[1:, 1])
print(numpy.array([[[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']]])[0:2, 0:2, 1])
# Specify or check data type of array object elements
print('dtype')
Arr = numpy.array([1, 2, 3, 4], dtype=numpy.int32)
print(Arr.dtype)
print('astype')
Arr = Arr.astype(numpy.int64)
print(Arr.dtype)
# Copy of array object owns the data inside it
print('copy')
Arr_Copy = Arr.copy()
Arr_Copy[3] = 3
Arr[1] = 1
print(Arr_Copy)
print(Arr)
# View of array object depends on original version
print('view')
Arr_View = Arr.view()
Arr_View[3] = 3
Arr[1] = 2
print(Arr_View)
print(Arr)
# Returns None if array object owns the data inside it, otherwise refers to the original array object
print('base')
print(Arr_Copy.base)
print(Arr_View.base)
# Returns number elements in each dimension (columns and rows)
print('shape')
print(Arr.shape)
print(numpy.shape([[1, 2], [3, 4]]))
print(numpy.shape([[[1], [2]], [[3], [4]]]))
print(numpy.shape([[[[1, 2], [3, 4]]]]))
# Returns a different view filled by array object elements
print('reshape')
print(Arr.reshape(4, 1))
# You can use only one unknown dimension and let numpy calculate the number
print(Arr.reshape(2, 2, -1))
# Returns a one-dimensional view of multi-dimensional array object
print(numpy.reshape([[1, 2], [3, 4]], -1))
# Iterate through all dimensions of array object
print('nditer')
Arr = numpy.array([[['AB'], ['CD']], [[12], [34]]])
for i in numpy.nditer(Arr):
    print(i)
for x in numpy.nditer(Arr[:, ::2]):
    print(x)
# Returns also the index of each element
print('ndenumerate')
for i, x in numpy.ndenumerate(Arr):
    print(i, x)
# Returns combination of multiple array objects
print('concatenate')
print(numpy.concatenate(([1, 2], [3, 4])))
print(numpy.concatenate(([[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']])))
print(numpy.concatenate(([[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']]), axis=1))
# Stack is concatenation done along a new axis (puts elements above eachother)
print('stack')
print(numpy.stack(([1, 2], [3, 4])))
print(numpy.stack(([[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']])))
print(numpy.stack(([[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']]), axis=1))
# Hstack is concatenation done along new rows
print('hstack')
print(numpy.hstack(([1, 2], [3, 4])))
print(numpy.hstack(([[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']])))
# Vstack is concatenation done along new columns
print('vstack')
print(numpy.vstack(([1, 2], [3, 4])))
print(numpy.vstack(([[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']])))
# Dstack is concatenation done along new height (depth)
print('dstack')
print(numpy.dstack(([1, 2], [3, 4])))
print(numpy.dstack(([[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']])))
# Splits array object into specified number of arrays
Arr = numpy.array([[[1, 2], [3, 4]], [['A', 'B'], ['C', 'D']]])
print('array_split')
print(numpy.array_split(Arr, 2))
print(numpy.array_split(Arr, 3))
print(numpy.array_split(Arr, 2, axis=1))
# split is array_split if there are enough elements
print('split')
print(numpy.split(Arr, 2))
# Hsplit is split done along new rows
print('hsplit')
print(numpy.hsplit(Arr, 2))
# Vsplit is split done along new columns
print('vsplit')
print(numpy.vsplit(Arr, 2))
# Dsplit is split done along new height (depth)
print('dsplit')
print(numpy.dsplit(Arr, 2))
# Returns which indexes fits the predicate
Arr = numpy.array([1, 2, 3, 4])
print('where')
print(numpy.where(Arr == 3))
print(numpy.where(Arr % 2 == 0))
# Returns the index where specified value should be inserted to keep the order
print('searchsorted')
print(numpy.searchsorted([1, 2, 3, 4], 2))
print(numpy.searchsorted([1, 2, 3, 4], 2, side='right'))
print(numpy.searchsorted([1, 2, 3, 4], [2, 4]))
# Returns a sorted copy of original array object
print('sort')
print(numpy.sort([3, 2, 1, 4]))
print(numpy.sort([[3, 2, 1, 4], ['A', 'C', 'B', 'D']]))
# Filtering is inserting specific elements of an array object into another one
print('filter')
Arr_Bool = [False, False, True, True]
print(Arr[Arr_Bool])
Arr_Bool = []
for i in Arr:
    if i > 2:
        Arr_Bool.append(True)
    else:
        Arr_Bool.append(False)
print(Arr[Arr_Bool])
Arr_Bool = Arr > 2
print(Arr[Arr_Bool])
# Returns specified amount of random numbers within specified range
print('randint')
print(numpy.random.randint(0, 100, 10))
print(numpy.random.randint(0, 100, size=(10)))
print(numpy.random.randint(0, 100, size=(2, 5)))
# Returns a float number between 0 and 1
print('rand')
print(numpy.random.rand())
print(numpy.random.rand(10))
print(numpy.random.rand(2, 5))
# returns specified amount of given elemet
print('choice')
print(numpy.random.choice(Arr))
print(numpy.random.choice(Arr, size=(10)))
print(numpy.random.choice(Arr, size=(2, 5)))
print(numpy.random.choice(Arr, size=(10), p=[0.125, 0.125, 0.125, 0.625]))
# Returns a re-arranged copy of original array object
print('shuffle')
numpy.random.shuffle(Arr)
print(Arr)
# Returns a re-arranged view of original array object
print('permutation ')
print(numpy.random.permutation(Arr))
# Numpy distribution and ufunc and more on is still left to check