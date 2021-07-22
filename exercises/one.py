import matplotlib.pyplot as plt
from functools import reduce
from math import cos, sin, pi

# *^*^*^*^*^*^*^*^*^*^*^*^
# From Quantum Mechanics for the Working Professional, Section 001
# This is a quick script extracted from a JuPyter Notebook
# *^*^*^*^*^*^*^*^*^*^*^*^

# define the factorial function
fact = lambda n : max(1,reduce(lambda x,y : max(x,1)*max(y,1) , range(n+1)))

# define the binomial coefficient
binomial = lambda N,n : fact(N) / fact(n) / fact(N-n)

# define the probabilty mass function for the binomial distribution for two relative cases up and down, given as ratios
PMF = lambda up, down : ( lambda N,n : binomial(N,n) * up**n * down**(N-n) / (up + down)**N)

# define the binomial distribution for a fair coin
uniform = PMF(0.5,0.5)

# define the binomial distribution for a theta-dependent coin
theta = lambda th : PMF(cos(th),sin(th))


def plotPMF( pmf , counts = 50 ):
    '''For a given PMF, plot the relative probabilities as a histogram.'''
    bins = range(counts + 1)
    data = [100*pmf(counts,n) for n in bins]
    
    plt.bar(bins,data)
    plt.xlabel("Number of times Spin Up")
    plt.ylabel("Percent Probability")
    plt.title("Plot of the Probability Mass Function for N = " + str(counts))
    
    
def plotPMFTheta( th , counts = 50 ):
    '''For a given value of theta, generate the relavant PMF and plot as a histogram.'''
    plotPMF( theta(th) , counts )
    plt.title("Plot of the Probability Mass Function for N = " + str(counts))


# *^*^*^*^*^*^*^*^*^*^*^*^
# Just a head's up:
# You'll need to either paste this in a notebook IDE or modify the code to save plots to disk.
# try the following commands:
# *^*^*^*^*^*^*^*^*^*^*^*^

for n in [10,50,100]:
    plotPMF(uniform,n)

for th in [pi/16,pi/8,pi/6,pi/5,pi/3,pi/2.2]:
    plotPMFTheta(th,50)
