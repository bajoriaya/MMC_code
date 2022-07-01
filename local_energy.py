
import numpy as np


# Step 3 of the assignment
# we are going to define a local energy for the matrix input, co-ordinates and values
# matrixx = the matrix, nodemat = the 2x2 matrix of the i and j positions of the vectors to find local energy
# you need eAA, eAB, eBB

def localenergy(matrixx, nodemat, eAA, eAB, eBB):
    # define k values as zero
    k = np.zeros((2, 6))


    # find the energy of the pair of vertexes
    for i in range(0, 2):
        if matrixx[nodemat[i, 0], nodemat[i, 1]] == 0:
            continue

        # if the position in the matrix has 1 then use these sets
        elif matrixx[nodemat[i, 0], nodemat[i, 1]] == 1:
            if matrixx[nodemat[i, 0], nodemat[i, 1] + 1] == 1:  # right edge
                k[i, 0] = eAA
            if matrixx[nodemat[i, 0], nodemat[i, 1] + 1] == 2:
                k[i, 0] = eAB
            if matrixx[nodemat[i, 0], nodemat[i, 1] + 1] == 0:
                k[i, 0] = 0
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1]] == 1:  # bottom edge
                k[i, 1] = eAA
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1]] == 2:
                k[i, 1] = eAB
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1]] == 0:
                k[i, 1] = 0
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1] - 1] == 1:  # bottom left edge
                k[i, 2] = eAA
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1] - 1] == 2:
                k[i, 2] = eAB
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1] - 1] == 0:
                k[i, 2] = 0
            if matrixx[nodemat[i, 0], nodemat[i, 1] - 1] == 1:  # left edge
                k[i, 3] = eAA
            if matrixx[nodemat[i, 0], nodemat[i, 1] - 1] == 2:
                k[i, 3] = eAB
            if matrixx[nodemat[i, 0], nodemat[i, 1] - 1] == 0:
                k[i, 3] = 0
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1]] == 1:  # top edge
                k[i, 4] = eAA
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1]] == 2:
                k[i, 4] = eAB
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1]] == 0:
                k[i, 4] = 0
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1] + 1] == 1:  # top right edge
                k[i, 5] = eAA
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1] + 1] == 2:
                k[i, 5] = eAB
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1] + 1] == 0:
                k[i, 5] = 0
        # if the position in the matrix has 2 then use these sets
        elif matrixx[nodemat[i, 0], nodemat[i, 1]] == 2:
            if matrixx[nodemat[i, 0], nodemat[i, 1] + 1] == 1:  # right edge
                k[i, 0] = eAB
            if matrixx[nodemat[i, 0], nodemat[i, 1] + 1] == 2:
                k[i, 0] = eBB
            if matrixx[nodemat[i, 0], nodemat[i, 1] + 1] == 0:
                k[i, 0] = 0
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1]] == 1:  # bottom edge
                k[i, 1] = eAB
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1]] == 2:
                k[i, 1] = eBB
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1]] == 0:
                k[i, 1] = 0
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1] - 1] == 1:  # bottom left edge
                k[i, 2] = eAB
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1] - 1] == 2:
                k[i, 2] = eBB
            if matrixx[nodemat[i, 0] + 1, nodemat[i, 1] - 1] == 0:
                k[i, 2] = 0
            if matrixx[nodemat[i, 0], nodemat[i, 1] - 1] == 1:  # left edge
                k[i, 3] = eAB
            if matrixx[nodemat[i, 0], nodemat[i, 1] - 1] == 2:
                k[i, 3] = eBB
            if matrixx[nodemat[i, 0], nodemat[i, 1] - 1] == 0:
                k[i, 3] = 0
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1]] == 1:  # top edge
                k[i, 4] = eAB
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1]] == 2:
                k[i, 4] = eBB
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1]] == 0:
                k[i, 4] = 0
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1] + 1] == 1:  # top right edge
                k[i, 5] = eAB
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1] + 1] == 2:
                k[i, 5] = eBB
            if matrixx[nodemat[i, 0] - 1, nodemat[i, 1] + 1] == 0:
                k[i, 5] = 0

    localE = np.sum(k)
    return localE


