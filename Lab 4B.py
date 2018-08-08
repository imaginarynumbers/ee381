# Probability Problem
# Three ball in five cans at random
# Each ball in a different can

import math

# Random number generator formula values

N = 10000 # norm
A = 4857  # adder
M = 8601  # multiplier
S = 0     # seed

sum = 0   # initialize counter
trial = 0 # number of trials

Can =  [0,0,0]

K = int(input('Enter the number of experiments. '))

for k in range(K): # Outer
    
    for i in range(3):
        S = (M * S + A) % N
        r = S/N # random numbers on [0,1)
    
        Can_Number = math.floor(r * 5 + 1)
        Can[i] = Can_Number
        
    print(Can)