import matplotlib.pyplot as plt
import numpy as np


from swappy import swappy
from initialize_matrix import initialize_matrix
from Energy_gen import energygen
from node_position import nodepos
from local_energy import localenergy
from metropolis_criteria import metcrit

# Initializing variables

# Size of lattice
n = 50

# Density
rho = .95

# fraction of A disks
f = 0.3

# Energies
eAA = -6
eAB = 3
eBB = -3

# Temperature
T = 300

# number of cycles
nmov = 1000


# we add an indicator to indicate what simulation we are doing
rnd = "1"
sim = "1"


########################################################################################################################
# Beginning of simulation
# initializing zero matricies and arrays
rej = 0
numcycle = np.zeros(nmov)
energypercycle = np.zeros(nmov)
accratio = np.zeros(nmov)


mcacept = 0

# Step 1 and 2 for the assignment
# generate the original matrix
matrixinit = initialize_matrix(n, rho, f)
# generate the same matrix but that will evolve through the for loop
matrixevolve = matrixinit

# generate a graph to show the initial positions of the matrix
fig1, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
min_val, max_val = 0, n + 2
init_plot = ax1.matshow(matrixinit, cmap='inferno', vmin=0, vmax=2)

# Step 3 of the assignment
# Calculate the initial energy and store it in initial energy
# We take the matrix energy as the matrix that will evolve during the program
matrixenergy = energygen(matrixinit, eAA, eAB, eBB)
initialenergy = matrixenergy.copy()

# metropolis loop
for i in range(0, nmov):

    # Step 4 of the assignment
    nodeposition = nodepos(matrixevolve, n)
    localEinit = localenergy(matrixevolve, nodeposition, eAA, eAB, eBB)

    # Step 4 of the assignment
    # swapping the elments in the matrix
    matrixevolve = swappy(matrixevolve, nodeposition, n)
    localEprop = localenergy(matrixevolve, nodeposition, eAA, eAB, eBB)

    # finding the difference in energy between the local proposed matrix and the initial matrix
    deltaE = localEprop - localEinit

    # Step 5 of the assignment
    if deltaE <= 0:

        # if the energy is lower then the configuration can move on
        # update the energy
        matrixenergy = matrixenergy + deltaE
        print("Move accepted")

    else:
        x = metcrit(deltaE, T)
        if x == True:

            # if the metropolis criteria is true then we move on and accept the matrix
            # update the energy
            matrixenergy = matrixenergy + deltaE
            mcacept = mcacept + 1
            print("Move accepted")

        else:
            # if the metropolis criteria is false then we move back to the original matrix
            swappy(matrixevolve, nodeposition, n)
            rej = rej + 1
            print("Move rejected")

    print("the total energy is", matrixenergy)
    print("the acceptance ratio is", ((i + 1 - rej) / (i + 1)))

    # update the energy and rejection counter
    energypercycle[i] = matrixenergy
    numcycle[i] = i
    accratio[i] = ((i + 1 - rej) / (i + 1))

# we find the final energy matrix to ensure it is the same as the calculated final energy matrix
finalmatrixenergy = energygen(matrixevolve, eAA, eAB, eBB)

# End of simulation
########################################################################################################################
# Step 6 of the assignment
# We now create the graphs and figures to display the result of the simulation

# initialising the graphs
plt.rcParams["figure.figsize"] = [8, 8]
plt.rcParams["figure.autolayout"] = True

# We plot the final lattice as the second plot
min_val, max_val = 0, n + 2
final_plot = ax2.matshow(matrixevolve, cmap='inferno', vmin=0, vmax=2)
fig1.suptitle("Simulation {sim} , round {round}".format(round=rnd, sim = sim), fontsize=20)
ax1.set_title("Initial configuration")
ax2.set_title("{numb} moves".format(numb=nmov))

# we are annotating the inputs
ax1.annotate \
    (" rho = {rpo} f = {prob} \n eAA = {enAA}, eBB = {enBB}, eAB = {enAB}, \
     \n T = {temp} K, nmov = {nmov}\n Red = A, Yellow = B, Black = empty". \
     format(rpo=rho, prob=f, enAA=eAA, enAB=eAB, enBB=eBB, \
            temp=T, nmov=nmov), xy=(0, -60.0), \
     annotation_clip=False, xycoords="axes points")

# we plot the total energy of the system per cycle
fig2, (ax3, ax4) = plt.subplots(nrows=2, ncols=1)
fig2.suptitle("Simulation {sim} , round {round}".format(round=rnd, sim=sim), fontsize=20)
ax3.set_title('Energy per Cycle vs number of cycles')
ax3.set_ylabel('Energy in kcal/mol')
energyplot = ax3.plot(numcycle, energypercycle, linewidth=5)

# we plot the acceptance ratio per cycle
accplot = ax4.plot(numcycle, accratio, linewidth=5)
ax4.set_title('Acceptance ratio vs number of cycles')
ax4.set_xlabel('Cycles (Millions)')
ax4.set_ylabel('Acceptance ratio')
ax4.annotate \
    (" rho = {rpo} f = {prob} \n eAA = {enAA} kcal/mol, eBB = {enBB} kcal/mol, eAB = {enAB} kcal/mol, \
     \n T = {temp}, K nmov = {nmov}". \
     format(rpo=rho, prob=f, enAA=eAA, enAB=eAB, enBB=eBB, \
            temp=T, nmov=nmov), xy=(0, -80.0), fontsize=12, \
     annotation_clip=False, xycoords="axes points")

plt.show()

# End of simulation