# step 4 of the assignment
# defining a swap function that will ammend the matrix with the new node values in the local energy calc, we are only
# using the positions of the matrix so we can swap the disks back if the move is rejected
# mat-> matrix in question
# np -> node position
# n -> size of matrix
def swappy(mat, np, n):
    # swaps the two positions of the matrix.
    x = mat[np[0, 0], np[0, 1]]
    mat[np[0, 0], np[0, 1]] = mat[np[1, 0], np[1, 1]]
    mat[np[1, 0], np[1, 1]] = x
    # # re-establish boundary conditions

    mat[0, 1:n + 1] = mat[n, 1:n + 1]
    mat[n + 1, 1:n + 1] = mat[1, 1:n + 1]
    mat[1:n + 1, 0] = mat[1:n + 1, n]
    mat[1:n + 1, n + 1] = mat[1:n + 1, 1]

    mat[0, n + 1] = mat[n, 1]
    mat[n + 1, 0] = mat[1, n]
    mat[0, 0] = mat[n, n]
    mat[n + 1, n + 1] = mat[1, 1]
    # returns the modified matrix for use

    return mat


