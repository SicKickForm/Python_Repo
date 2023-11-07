import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Matplotlib module methods
# Matplotlib is a low level graph plotting module that serves as a visualization utility
print("__version__")
print(matplotlib.__version__)
X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
Y = np.array([1, 0, 9, 4, 25, 16, 49, 36, 81, 64])
# Use plot() to connect the coordinates in a diagram
print("plot")
plt.plot(X, Y)
plt.show()
# X axis is [0, 1, 2, ...] by default
# Use "o" to draw only markers in a diagram
plt.plot(Y, "o")
plt.show()
# You can customize markers, linestyles and colors
plt.plot(X, Y, marker="*", ls="dashed", c="hotpink")
plt.show()
# You can also use formatted string notation "marker|linestyle|color"
plt.plot(X, Y, "P:b")
plt.show()
# You can customize marker's size, edge and face color
plt.plot(X, Y, ".", ms=15, mec="k", mfc='c')
plt.show()
# You can customize line's width
plt.plot(X, Y, lw=10)
plt.show()
# You can customize diagram's label, title, font and grid
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
my_font = {'family':'serif','color':'blue','size':20}
plt.title("Title", fontdict=my_font, loc="left")
# You can set grid's for each axis
plt.grid(axis="both")
plt.plot(X, Y)
plt.show()
# Use subplot(rows, columns, index) to have multiple plots in the same diagram
plt.subplot(1,2,1)
plt.plot(X, Y)
plt.subplot(1,2,2)
plt.plot(X, Y)
# You can set a super title for all subplots
plt.suptitle("Super title")
plt.show()
# Use scatter() to draw markers in a diagram
X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
Y = np.array([1, 0, 9, 4, 25, 16, 49, 36, 81, 64])
A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
B = np.array([2, 0, 6, 4, 10, 8, 14, 12, 18, 16])
plt.scatter(X, Y)
# You can compare multiple scatter plots in the same diagram
plt.scatter(A, B)
plt.show()
# You can customize markers's color, transparency and size
plt.scatter(X, Y, c="g", alpha=0.4, s=15)
plt.show()
# You can set a unique color for each marker
my_colors = np.array(["b", "g", "r", "k", "c", "yellow", "hotpink", "gray", "olive", "purple"])
plt.scatter(A, B, c=my_colors)
plt.show()
# You can use built-in color maps for the markers
my_colors = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
plt.scatter(X, Y, c=my_colors, cmap="viridis")
# You can see color map's color bar
plt.colorbar()
plt.show()
# Use bar() to display quantity of each category
X = np.array(["A", "B", "C", "D"])
Y = np.array([13, 8, 17, 5])
# You can customize bar's width and color
plt.bar(X, Y, width= 0.5, color="c")
plt.show()
# You can also have horizental bars 
plt.barh(X, Y, height= 0.5)
plt.show()
# Use hist() to display distribution
X = np.random.normal(10, 10, 50)
plt.hist(X)
plt.show()
# Use pie() to display percential
X = np.random.normal(10, 10, 4)
plt.pie(X)
plt.show()
# You can set labels for each item and change the startangle (0 by default)
plt.pie(X, labels=["A", "B", "C", "D"], startangle=90)
# You can set a category explanation
plt.legend(title= "Names")
plt.show()
# You can also customize each item
plt.pie(X, labels=["A", "B", "C", "D"], explode=[0.25, 0, 0, 0], shadow=True)
plt.show()
