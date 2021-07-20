import numpy as np


A = np.array([[-1,4],[2,-2]])

# calculating eigen values and vector, by numpy eig methods which,
# returns  a vector of eigenalues and a matrix of eigenvectos


lambdas, V = np.linalg.eig(A)
print(lambdas)

# The matrix contains as many eigenvectors as there are columns of A:
print(V)

# satisfies the the equation Av = yv for the first eigenvector

# get first columns of vector V, and first eigenvalue
v = V[:,0]
eval = lambdas[0]
Av = np.dot(A ,v)
print(Av)

# now multiply lambda to vec v
print(eval * v)

from plot_vectors import plot_vectors
import matplotlib.pyplot as plt
plot_vectors([Av,v],['blue','lightblue'])
plt.xlim(-1,2)
_ = plt.ylim(-1,2)
plt.show()