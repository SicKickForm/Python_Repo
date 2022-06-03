import numpy
from scipy import constants
from scipy.optimize import root, minimize
from scipy.sparse import csr_matrix, csc_matrix
from scipy.sparse import csgraph
from scipy.sparse.csgraph import connected_components
# Scipy provides utility functions for optimization, stats and signal processing
# Scipy uses numpy underneath it's computation
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
#
