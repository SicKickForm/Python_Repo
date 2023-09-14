from math import sin
from scipy.optimize import minimize

# Minimize

Degree = int(input("Enter your degree: "))

def Eqn(X):
    return X**2 + sin(X) + 3

print(minimize(Eqn, Degree, method='BFGS'))