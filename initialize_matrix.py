import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np
import random

# Step 1 and 2 of assignment
# This function creates an n by n matrix with density rho and probability of A (or 1) as p.

def initialize_matrix(n, rho, f):

    # create a 2D triangular lattice with empty disks represented by zeros with probability of 1 - rho
    # disk A represented by 1 with a probability of f * rho
    # disk B represented by 2 with a probability of (1-f) * rho

    # we initialize the matrix
    mat = np.random.choice([0, 1, 2], size=n*n, p=[1-rho, f*rho, (1 - f)*rho]).reshape(n, n)

    # In order to create the boundary conditions I have added an additional layer of node
    matinit = np.zeros((n + 2, n + 2))

    # combining the zero matrix and the initial matrix of 'disks'
    matinit[1:n + 1, 1:n + 1] = mat

    # establishing boundary conditions of the edge of the matrix
    matinit[0, 1:n+1] = matinit[n, 1:n+1]
    matinit[n + 1, 1:n+1] = matinit[1, 1:n+1]
    matinit[1:n+1, 0] = matinit[1:n+1, n]
    matinit[1:n+1, n + 1] = matinit[1:n+1, 1]

    # establishing the boundary conditionals of the diagonals
    matinit[0, n + 1] = matinit[n, 1]
    matinit[n + 1, 0] = matinit[1, n]
    matinit[0, 0] = matinit[n, n]
    matinit[n + 1, n + 1] = matinit[1, 1]

    return matinit