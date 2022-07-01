
import numpy as np


# inputs

# generation of the total energy
def energygen(matrix, eAA, eAB, eBB):
    # Creates a matrix of zeros of nxn (the -2 omits the boundary conditions)
    # this will be populated with the energies
    emat = np.zeros((len(matrix) - 2, len(matrix) - 2))

    # initialise k values of zero
    k1, k2, k3, = 0, 0, 0

    # for loop to iterate across the "inner" matrix of values
    # length of the matrix is n+2
    # but due to python the element of the n+2 is called n+1, this takes the 2nd - n+1 row
    # we are iterating for three energies assigned to each vertex with respect to the other disks surrounding it.
    # this is to avoid double counting
    # we are setting a counter to count the number of
    numEAA = 0
    numEAB = 0
    numEBB = 0

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix)-1):
            if matrix[i, j] == 0:
                continue
            if matrix[i, j] == 1:  # defines k1 - k3 depending the energy assigned
                if matrix[i, j + 1] == 1:  # right edge
                    k1 = eAA
                    numEAA = numEAA + 1
                if matrix[i, j + 1] == 2:
                    k1 = eAB
                    numEAB = numEAB + 1
                if matrix[i, j + 1] == 0:
                    k1 = 0
                if matrix[i + 1, j] == 1:  # bottom edge
                    k2 = eAA
                    numEAA = numEAA + 1
                if matrix[i + 1, j] == 2:
                    k2 = eAB
                    numEAB = numEAB + 1
                if matrix[i + 1, j] == 0:
                    k2 = 0
                if matrix[i + 1, j - 1] == 1:  # bottom left edge
                    k3 = eAA
                    numEAA = numEAA + 1
                if matrix[i + 1, j - 1] == 2:
                    k3 = eAB
                    numEAB = numEAB + 1
                if matrix[i + 1, j - 1] == 0:
                    k3 = 0
            if matrix[i, j] == 2:  # same thing but with molecule 'B'
                if matrix[i, j + 1] == 1:  # right edge
                    k1 = eAB
                    numEAB = numEAB + 1
                if matrix[i, j + 1] == 2:
                    k1 = eBB
                    numEBB = numEBB + 1
                if matrix[i, j + 1] == 0:
                    k1 = 0
                if matrix[i + 1, j] == 1:  # bottom edge
                    k2 = eAB
                    numEAB = numEAB + 1
                if matrix[i + 1, j] == 2:
                    k2 = eBB
                    numEBB = numEBB + 1
                if matrix[i + 1, j] == 0:
                    k2 = 0
                if matrix[i + 1, j - 1] == 1:  # bottom left edge
                    k3 = eAB
                    numEAB = numEAB + 1
                if matrix[i + 1, j - 1] == 2:
                    k3 = eBB
                    numEBB = numEBB + 1
                if matrix[i + 1, j - 1] == 0:
                    k3 = 0

            # k1,k2,k3 values are now assigned. We sum the k1 - k3 to create a dummy energy for each vertex
            # note that this vertex does not actually have an energy value
            emat[i - 1, j - 1] = k1 + k2 + k3

            # reassign k's to zero ready for next loop
            k1, k2, k3 = 0, 0, 0

    # sum all the energies into one energy value
    energyval = np.sum(emat)
    return energyval



