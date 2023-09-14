import matplotlib.pyplot as plt
import numpy
from scipy import constants
from scipy.optimize import root, minimize
from scipy.sparse import csr_matrix, csc_matrix
from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall, bellman_ford, depth_first_order, breadth_first_order
from scipy.spatial import KDTree, Delaunay, ConvexHull
from scipy.spatial.distance import euclidean, cityblock, cosine, hamming

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

