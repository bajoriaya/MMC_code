import numpy as np
import random


# Step 5 of the assignment
# defining a metropolis criteria where the delta energy is higher
def metcrit(deltaen, T):
    R = random.uniform(0, 1)

    if R < np.exp(-deltaen / (0.001985875 * T)):
        # if the R is smaller than the criteria, we accept the move
        metcrit = True
    else:
        # if the R is bigger then we reject the move - we would then
        metcrit = False
    return metcrit
