# Modules
# Python has built-in standard modules, importable modules and external modules
# Install external module A from PyPI (Python package index) using
# py -m pip --install A command on terminal
# Use py -m pip --h for more commands
# You can create modules by saving a file with .py format
# You can call modules using import command
# Use import module as A command to rename module to A
# Use from module import A command to call only A from module
# When using from method don't refer to module other functions and variables
# Use module.A command to use A from module
# Use dir(A) function to get all methods and variables in module A

# Built-in modules
import platform
import datetime as Date
import math
import json
import re
import itertools
import numpy
from scipy import constants
from scipy.optimize import root, minimize
from scipy.sparse import csr_matrix, csc_matrix
from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall, bellman_ford, depth_first_order, breadth_first_order
from scipy.spatial import KDTree, Delaunay, ConvexHull
from scipy.spatial.distance import euclidean, cityblock, cosine, hamming
import matplotlib.pyplot as plt

# Platform module methods
# Platform module includes Your device's specs information
print(platform.__builtins__)
print(platform.__cached__)
print(platform.__file__)
print(platform.__name__)
print(platform.__version__)
platform.__doc__
platform.__loader__
platform.__package__
platform.__spec__
print(platform.release())
print(platform.processor())
print(platform.sys)
print(platform.system())
print(platform.uname())
print(platform.version())
print(platform.win32_edition())
print(platform.win32_is_iot())
print(platform.win32_ver())
print(platform.machine())
print(platform.node())
print(platform.platform())
print(platform.java_ver())
print(platform.mac_ver())
print(platform.python_branch())
print(platform.python_build())
print(platform.python_compiler())
print(platform.python_implementation())
print(platform.python_revision())
print(platform.python_version())
print(platform.python_version_tuple())
platform.architecture()
platform.uname_result
platform.freedesktop_os_release
platform.system_alias

# Datetime module methods
# Datetime module includes various methods to show date and time
# Use datetime() constructor command Create time objects
# You can create time objects up to micro seconds
print(Date.date(2003, 1, 17))
print(Date.time(19, 37))
print(Date.datetime(2003, 1, 17, 19, 37))
print(Date.datetime.now())
print(Date.datetime.now().year)
print(Date.datetime.now().month)
print(Date.datetime.now().day)
print(Date.datetime.now().weekday())
print(Date.datetime.now().hour)
print(Date.datetime.now().minute)
print(Date.datetime.now().second)
print(Date.datetime.now().microsecond)
# Use strftime command to format date objects into readable strings
# strftime methods
# Date and time methods
print(Date.datetime.now().strftime('%c'))
print(Date.datetime.now().strftime('%x'))
print(Date.datetime.now().strftime('%X'))
# Year methods
print(Date.datetime.now().strftime('%C'))
print(Date.datetime.now().strftime('%G'))
print(Date.datetime.now().strftime('%Y'))
print(Date.datetime.now().strftime('%y'))
# Month methods
print(Date.datetime.now().strftime('%B'))
print(Date.datetime.now().strftime('%b'))
print(Date.datetime.now().strftime('%m'))
# Week methods
print(Date.datetime.now().strftime('%U'))
print(Date.datetime.now().strftime('%W'))
print(Date.datetime.now().strftime('%V'))
# Day methods
print(Date.datetime.now().strftime('%A'))
print(Date.datetime.now().strftime('%a'))
print(Date.datetime.now().strftime('%j'))
print(Date.datetime.now().strftime('%d'))
print(Date.datetime.now().strftime('%w'))
print(Date.datetime.now().strftime('%u'))
# Hour methods
print(Date.datetime.now().strftime('%H'))
print(Date.datetime.now().strftime('%I'))
print(Date.datetime.now().strftime('%p'))
# Minute method
print(Date.datetime.now().strftime('%M'))
# Second method
print(Date.datetime.now().strftime('%S'))
# Micro second method
print(Date.datetime.now().strftime('%f'))
print(Date.datetime.now().strftime('%%'))

# Math module methods
# Math module includes various arithmetical subjects and operators
print(math.e)
print(math.inf)
print(math.nan)
print(math.pi)
print(math.tau)
# Any
print(math.tan(90))
print(math.tanh(90))
print(math.atan(90))
print(math.atan2(1, 1))
print(math.sinh(60))
print(math.asinh(60))
print(math.cosh(30))
print(math.erf(5))
print(math.erfc(5))
print(math.fmod(11, 6))
print(math.exp(5))
print(math.expm1(5))
print(math.frexp(5))
print(math.ldexp(1.25, 2))
print(math.ceil(4.4))
print(math.trunc(5.4))
print(math.floor(5.6))
print(math.comb(5, 4))
print(math.perm(5, 4))
print(math.factorial(5))
print(math.pow(5 ** (1 / 2), 2))
print(math.sqrt(25))
print(math.gcd(15, 25))
print(math.remainder(5, 4))
print(math.copysign(-5, 2))
print(math.fabs(-5))
print(math.isclose(1.25, 1.251))
print(math.isfinite(0))
print(math.isinf(1))
print(math.isnan(1))
# W
print(math.gamma(5))
print(math.lgamma(5))
print(math.isqrt(26))
print(math.log(1))
print(math.log10(100000))
print(math.log1p(0))
print(math.log2(1))
# W - (1 , 0)
print(math.acosh(1))
# [-1 , +1]
print(math.acos(-1))
print(math.asin(1))
print(math.cos(0))
print(math.sin(0))
# (-1 , +1)
print(math.atanh(0.5))
# Angle
print(math.degrees(math.pi))
print(math.radians(90))
# Coordinated point
print(math.dist((3, 4), (0, 0)))
print(math.hypot(3, 4))
# Array
print(math.fsum((1, 2, 2)))
print(math.prod([5]))

# Json module methods
# JSON is an object similar to dictionaries containing plain data
# Json module includes various methods to store and exchange Json (Java
# Script object notation) data
# converting json type data into a python dictionary
Json_Type_Info = '{"Name" : "SicKickForm", "Age" : 18}'
Python_Dict_Info = json.loads(Json_Type_Info)
# When You convert from Python to Json objects change to Json equivalent
# Python    JSON
# dict 	 =  Object
# list 	 =  Array
# tuple  =  Array
# str 	 =  String
# int 	 =  Number
# float  =  Number
# True   =  true
# False  =  false
# None   =  null
Json_Type_Info2 = json.dumps(Python_Dict_Info)
Info = {
    "Name": "SicKickForm",
    "Age": 18,
    "Sensitive": False,
    "Friends": ("Dia", "akaTeen"),
    "Interests": None,
    "Languages": [
        {"Name": "Python", "Level": "Inter mediate"},
        {"Name": "Java", "Level": "Basic"}
    ]
}
print(json.dumps(Info))
# Use the indent parameter to specify numbers of indents to output
# Use the separators parameter to set a separator
# Default separator is (", ",": ")
# Use sort-keys command to specify is the keys should be ordered or not
print(json.dumps(Info, indent=1, separators=(', ', ': ',), sort_keys=True))
# load() function is to read Json data from a file and convert to Python dict
# dump() function is to read Python file and convert to Json file

# RegEx module methods
# Use RegEx to check if a string contains the specified search pattern
Info = 'SicKickForm of human kind is a nickname for a 18 years old boy'
print(re.search('SicKickForm', Info))
print(re.search('SicKickForm', Info).span())
print(re.search('SicKickForm', Info).string)
print(re.search('SicKickForm', Info).group())
print(re.findall('f', Info))
print(re.split('i', Info, 3))
print(re.sub('i', '/', Info, 3))
# RegEx meta characters
# Lower case charcaters in the domain
print(re.findall('[a-h]', Info))
print(re.findall('[abc]', Info))
print(re.findall('[12345]', Info))
# Single digits in the domain
print(re.findall('[6-9]', Info))
# Double digits in the domain
print(re.findall('[1-5][5-8]', Info))
# Lower and upper case charcaters in the domain
print(re.findall('[a-hA-L]', Info))
# Except given characters
print(re.findall('[^abc]', Info))
# Any character in the blank spot
print(re.findall('o.', Info))
# Zero or more characters in the blank sport
print(re.findall('i.*F', Info))
# One or more characters in the blank sport
print(re.findall('i.+F', Info))
# Zero or one characters in the blank sport
print(re.findall('i.?F', Info))
# Specified amount of  characters in the blank sport
print(re.findall('i.{2}F', Info))
# Starting with
print(bool(re.search('^S', Info)))
# Ending with
print(bool(re.search('y$', Info)))
# Either or
print(re.findall('boy|girl', Info))
# Special charcaters
# Start of string
print(bool(re.search('\ASicK', Info)))
# Start or end of a word
print(bool(re.search(r'\bSicK', Info)))
print(bool(re.search(r'Form\b', Info)))
# Middle of a word
print(bool(re.search(r'\BKick', Info)))
# End of a word
print(bool(re.search('boy\Z', Info)))
# Digits of String
print(re.findall('\d', Info))
# String without digits
print((re.findall('\D', Info)))
# Spaces of string
print(re.findall('\s', Info))
# String without spaces
print(re.findall('\S', Info))
# Letters digits underscores of string
print(re.findall('\w', Info))
# String without letters digits underscores
print(re.findall('\W', Info))

# Itertools module methods
# Counting up to infinite using specified step
print('count')
IT_List = []
for i in itertools.count(1, 1):
    IT_List.append(i)
    if i == 4:
        print(IT_List)
        break
# Iterate through an iterable infinitely
print('cycle')
for i in itertools.cycle(IT_List):
    print(IT_List)
    break
# Repeat an object infinite or specified times
print('repeat')
print(list(itertools.repeat(IT_List, 3)))
# Returns a running total of values and indexes
print('accumulate')
print(list(itertools.accumulate(range(4))))
# Returns values from iterable that fit the predicate
print('takewhile')
print(list(itertools.takewhile(lambda X: X <= 4, range(50))))
# Returns a long iterable containing all specified iterables elements
print('chain')
print(list(itertools.chain(range(1), range(1, 4))))
# Returns a long iterable containing all specified iterable elements
print('chain.from_iterable')
print(list(itertools.chain.from_iterable('AB' 'CD')))
# Returns first iterable elemnets if same index in second iterable is True
print('compress')
print(list(itertools.compress('ABCD', (True, True, False, False))))
# Returns iterable elements after that specified predicate becomes Flase
print('dropwhile')
print(list(itertools.dropwhile(lambda X: X < 2, range(4))))
# Returns iterable elements that are False in specified predicate
print('filterfalse')
print(list(itertools.filterfalse(lambda X: X % 2 == 0, range(4))))
# Returns keys from iterable attached to function groups
print('groupby')
print(list(itertools.groupby(range(4), lambda X: X)))
# Returns specified iterable element
print('islice')
print(list(itertools.islice('AAABBBCCCDDD', 0, 11, 3)))
# Returns each iterable element with next element
print('pairwise')
print(list(itertools.pairwise('ABCD')))
# Retuens iterable elements with the specified function applied
print('starmap')
print(list(itertools.starmap(lambda X: X, 'ABCD')))
# Divides iterable to specified number of iterables
print('tee')
print(list(itertools.tee('ABCD', 3)))
# Returns iterable elements with same index together
print('zip_longest')
print(list(itertools.zip_longest('AB', 'CD')))
# Returns the combination of two iterables
print('product')
print(list(itertools.product('ABCD', range(4))))
# Returns the permutations of iterable with specified length
print('permutations')
print(list(itertools.permutations('ABCD', 2)))
# Returns combinations of iterable with specified length
print('combinations')
print(list(itertools.combinations('ABCD', 2)))
# Returns combinations of iterable with specified length with repeat allowed
print('combinations_with_replacement')
print(list(itertools.combinations_with_replacement('ABCD', 2)))

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

# Scipy provides utility functions for optimization, stats and signal processing
# Scipy uses numpy underneath it's computation
# Scipy module methods
# Returns standard equivalent of specified contants
print('constants')
print(f'''Metric: {constants.kilo} , {constants.femto}
Binary: {constants.kibi} , {constants.exbi}
Mass: {constants.pound} , {constants.u}
Angle: {constants.degree} , {constants.arcmin}
Time: {constants.day} , {constants.Julian_year}
Length: {constants.inch} , {constants.light_year}
Pressure: {constants.mmHg} , {constants.bar}
Area: {constants.hectare} , {constants.acre}
Volume: {constants.liter} , {constants.barrel}
Speed: {constants.kmh} , {constants.speed_of_light}
Temperature: {constants.zero_Celsius} , {constants.degree_Fahrenheit}
Energy: {constants.eV} , {constants.erg}
Power: {constants.hp} , {constants.horsepower}
Force: {constants.dyn} , {constants.kgf}''')
# Optimizers either find the minimum value of a function or the root of an equation
# All algorithms in Machine Learning are complex equations that need to be minimized with given data


def Eqn(X):
    return X**2 + 2*X + numpy.cos(X)


# Returns root of equation
print('root')
print(root(Eqn, 0).x)
print(root(Eqn, 0))
# Returns minimum value of equation
# Usable methods are: 'CG', 'BFGS', 'Newton-CG', 'L-BFGS-B', 'TNC', 'COBYLA', 'SLSQP'
print('minimize')
print(minimize(Eqn, 0, method='BFGS').x)
print(minimize(Eqn, 0))
# Data that has mostly unused elements and no information (mostly 0) is called sparse data
# Data that carries mostly meaningful information (mostly non-0) is called dense data
# Returns meaningful elements with their index in column
print('csc_matrix')
print(csc_matrix(numpy.array([[0, 1], [0, 2], [0, 0], [1, 2]])))
print(csc_matrix(numpy.array([[0, 1], [0, 2], [0, 0], [1, 2]])).data)
# Returns meaningful elements with their index in row
print('csr_matrix')
print(csr_matrix(numpy.array([[0, 1], [0, 2], [0, 0], [1, 2]])))
print(csr_matrix(numpy.array([[0, 1], [0, 2], [0, 0], [1, 2]])).data)
# Returns number of meaningful (non-0) elements
print('count_nonzero')
print(csr_matrix(numpy.array(
    [[0, 1], [0, 2], [0, 0], [1, 2]])).count_nonzero())
# Removes 0-entries from the matrix
print('eliminate_zeros')
csr_matrix(numpy.array([[0, 1], [0, 2], [0, 0], [1, 2]])).eliminate_zeros()
# Removes duplicate entries from the matrix
print('sum_ducplicates')
csr_matrix(numpy.array([[0, 1], [0, 2], [0, 0], [1, 2]])).sum_duplicates()
# Returns meaningful elements with their index in column
print('tocsc')
print(csr_matrix(numpy.array([[0, 1], [0, 2], [0, 0], [1, 2]])).tocsc())
# Returns meaningful elements with their index in row
print('tocsr')
print(csc_matrix(numpy.array([[0, 1], [0, 2], [0, 0], [1, 2]])).tocsr())
# Adjacency matrixes explain a graph with different bound weight
# Returns all of the connected components in graph
Arr = numpy.array([[0, 1, 2], [1, 0, 0], [2, 0, 0]])
print('connected_components')
print(connected_components(csr_matrix(Arr)))
# Returns the shortest path in graph from one element to another
print('dijkstra')
print(dijkstra(Arr, return_predecessors=True, indices=0, limit=2))
# Returns the shortest path between all elements
print('floyd_warshall')
print(floyd_warshall(Arr, return_predecessors=True))
print('bellman_ford')
print(bellman_ford(Arr, return_predecessors=True, indices=0))
# Returns a depth first traversal from a node
print('depth_first_order')
print(depth_first_order(Arr, 1))
# Returns a breadth first traversal from a node
print('breadth_first_order')
print(breadth_first_order(Arr, 1))
# Spatial data refers to data that is represented in a geometric (coordinated) way
# Returns the KDtree object of closest point to specified point
print('KDtree')
Points = numpy.array([[0, 2], [3, 1], [-1, 2], [1, 2]])
KDT = KDTree(Points)
# Returns the shortest distance from specified point from KDtree object
print('query')
print(KDT.query((2, 1)))
# Returns triangulations of the specified polygon
print('Delaunay')
Points = numpy.array([[2, 4], [3, 4], [3, 0], [2, 2], [4, 1]])
Simplices = Delaunay(Points).simplices
plt.scatter(Points[:, 0], Points[:, 1], color='r')
plt.show()
plt.triplot(Points[:, 0], Points[:, 1], Simplices)
plt.show()
# Returns the smallest polygon that includes all the points
print('ConvexHull')
Points = numpy.array([[2, 4], [3, 0], [4, 1], [1, 2], [3, 1], [1, 2], [0, 2]])
plt.scatter(Points[:, 0], Points[:, 1])
plt.show()
for simplex in ConvexHull(Points).simplices:
    plt.plot(Points[simplex, 0], Points[simplex, 1], 'k-')
plt.show()
# Distance Matrixes explain differences between two points
# Returns euclidean distance between two points
print('euclidean')
print(euclidean((-1, 4), (2, 9)))
# Returns 4-directional distance between two points
print('cityblock')
print(cityblock((-1, 4), (2, 9)))
# Returns cosine angle between two points
print('cosine')
print(cosine((-1, 4), (2, 9)))
# Returns distance between binary sequences
print('hamming')
print(hamming((True, False, True), (False, True, True)))

# Pandas methods
# Creating data columns in pandas
print("Series")
Nums = [1, 3, 5, 7, 9]
print(pd.Series(Nums))
print(pd.Series(Nums)[1:4])
# Changing items' labels
print(pd.Series(Nums, index=["A", "B", "C", "D", "E"]))
# Creating key/value pandas objects
print("Key/Value object")
Team = {
    "Member1": "Dia",
    "Member2": "SicKickForm",
    "Member3": "akaTeen"}
print(pd.Series(Team))
# Returns specified labels
print(pd.Series(Team, index=["Member1", "Member3"]))
# Creating 2-dimensional data
print("DataFrame")
Team = {
    "Name": ["Dia", "SicKickForm", "akaTeen"],
    "Age": [17, 18, 22]}
print(pd.DataFrame(Team, index=["Member1", "Member2", "Member3"]))
# Returns specified rows
print(pd.DataFrame(Team).loc[0:1])
# One way to store big data sets is using JSON
# JSON is an object similar to dictionaries containing plain data
print("read_json")
print(pd.read_json("https://www.w3schools.com/python/pandas/data.js"))
# Comma separated file (CSV) is another simple way to store big data sets
print("read_csv")
Data = pd.read_csv("https://www.w3schools.com/python/pandas/dirtydata.csv.txt")
print(Data)
# The maximum amount of rows is defined in Pandas option settings
print("pd.options.display.max_rows")
print(pd.options.display.max_rows)
# You can change this number to remove the limit
pd.options.display.max_rows = 100
print(pd.options.display.max_rows)
# Returns headers and specified amount of rows from top (5 by default)
print("head")
print(Data.head(10))
# Returns headers and specified amount of rows from buttom (5 by default)
print("tail")
print(Data.tail(10))
# Returns information about data set
# The non-null number shows the rows with value in that header
# Rows without value in a header are bad for analysis and should be cleaned
print("info")
print(Data.info())
# Data cleaning
# Empty cells, Data in wrong format, Wrong data and Duplicates are bad data
# Cleaning empty cells
# Removing rows with empty cells in a new data set
# Use inplace=True statement to remove rows from original data set
print("dropna")
print(Data.dropna())
# Filling empty cells with given value in a new data set
# Use inplace=True statement to fill empty cells with given value in original data set
print("fillna")
print(Data.fillna(130))
# Filling empty cells of specified column with given value
print(Data["Calories"].fillna(130))
# Calculates the average of all values
print("mean")
Mean = Data["Calories"].mean()
print(Data["Calories"].fillna(Mean, inplace=True))
# Returns the center number after sorting the values ascending
print("median")
print(Data["Calories"].median())
# Returns the most frequent value
print("mode")
print(Data["Calories"].mode())
# Cleaning Data in wrong format
# Converting all cells in a column into the same data format
print("to_datetime")
print(pd.to_datetime(Data["Date"]))
# Unconvertable rows should be removed
print("subset")
Data["Date"] = pd.to_datetime(Data["Date"])
print(Data.dropna(subset=["Date"]))
# Cleaning wrong data
# Replacing wrong data
print("loc")
Data.loc[7, "Duration"] = 45
print(Data)
# You can use loops to replace values in big data sets
for i in Data.index:
    if Data.loc[i, "Duration"] < 60:
        Data.loc[i, "Duration"] = 60
print(Data)
# Removing rows with wrong data
print("drop")
Data.drop(7, inplace=True)
print(Data)
# Cleaning duplicates
# Returns True if a row is duplicate
print("duplicated")
print(Data.duplicated())
print("drop_duplicates")
print(Data.drop_duplicates(inplace=True))
print(Data)
# Calculates the statistical relationship between columns in data set
# Correlation table number between two columns varies from -1 to +1
# In a perfect +1 Correlation both values in a row either go up or go down
# In a perfect -1 Correlation one row's value goes up and the other row's value goes down
# If number gets close to 0 (after +/- 0.6) it's not a good Correlation anymore
# Not-numeric columns will be ignored
print("corr")
Data = pd.read_csv("https://www.w3schools.com/python/pandas/data.csv.txt")
print(Data.corr())
Data = pd.read_csv("https://www.w3schools.com/python/pandas/data.csv.txt")
Data.plot()
plt.show()
Data.plot(kind='scatter', x='Duration', y='Calories')
plt.show()
Data["Duration"].plot(kind='hist')
plt.show()

del Json_Type_Info, Json_Type_Info2, Python_Dict_Info, IT_List, i, x,
Arr, Arr_Copy, Arr_View, Arr_Bool, Eqn, Points, KDT, Simplices, Nums, Team, Data, Mean

