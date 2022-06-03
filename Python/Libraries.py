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
print(list(itertools.repeat(IT_List, 1)))
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

del Json_Type_Info, Json_Type_Info2, Python_Dict_Info, IT_List, i, x,
Arr, Arr_Copy, Arr_View, Arr_Bool, Eqn
