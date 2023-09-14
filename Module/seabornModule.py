import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn is a python data visualization library
print('distplot')
Data = [1, 1, 2, 3, 4, 5, 6, 6]
sns.distplot(Data)
plt.show()
sns.distplot(Data, hist=False)
plt.show()




