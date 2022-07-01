import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np
import random as random
from initialize_matrix import initialize_matrix

# Step 4 of the assignment - find a random disk and a random vertex (disk or no disk)

# matrixx -> the matrix itself, n -> the size of the matrix
def nodepos(matrixx,n):

    # here we are defining a 2x2 matrix with the co-ordinates of node 1 and node 2
    nodemat = np.zeros((2, 2))

    # here we are defining a 2x1 matrix with the values of node 1 and 2
    vval = np.zeros((2, 1))

    # here we find the non zero elements of the matrix
    y = np.nonzero(matrixx[1:n + 1, 1:n + 1])  # NB: the column and row numbering begins from zero at the row 1.
    y = np.transpose(y)


    # we identify a random number to mark the row we are interested in, rows start from zero
    rand = random.randint(0, len(y) - 1)

    # take the number of the original row and co-ordinate and store it in a dummy variable
    # note that i am taking +1 because the y is the matrix without the boundary conditions.
    # first column of y is i and second column is j, +1 to move back to coord with boundary conditions
    i1 = y[rand, 0] + 1
    j1 = y[rand, 1] + 1

    v1val = matrixx[i1, j1]

    # find a random value of a node in the matrix
    i2 = random.randint(1, len(matrixx) - 2)
    j2 = random.randint(1, len(matrixx) - 2)
    v2val = matrixx[i2, j2]

    # while the nodes are the same we repeat the process until we get a new value that is not the same.
    # vertex 2 cannot be the same as vertex 1
    while i1 == i2 and j1 == j2:
        i2 = random.randint(1, len(matrixx) - 2)
        j2 = random.randint(1, len(matrixx) - 2)
        v2val = matrixx[i2, j2]

    vval[0, 0], vval[1, 0] = v1val, v2val
    nodemat[0, 0], nodemat[0, 1], nodemat[1, 0], nodemat[1, 1] = i1, j1, i2, j2
    nodemat = nodemat.astype(int)

    # returns the co-ordinates and the value of the two nodes to swap (make sure you define as such)
    # nodemat - 2x2 matrix of the i and j positions of the matrix.
    return nodemat



