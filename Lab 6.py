# Simulation of a binomial random variable.
# This simulation will use the sum of bernoulli r.v.'s
# to simulate a the binomial r.v.

import random


n = 5       # the number of trials
x = 3       # the number of successes
p = 0.7     # the probability of success any outcome

N = 100     # the number of times the processes is repeated

trials = [0] 
trials = trials*n   # an empty trial list

j = 0               # accumulator initialized

for k in range(N):          # outside loop
    
    for i in range(n):      # inside loop, the individual experiments
    
        # Generation of Bernoulli random variables
        r = random.uniform(0,1) 
        if r < p:
            trials[i] = 1   # success
        else:
            trials[i] = 0   # failure
    #print(trials)          # print each of the trials
    s = sum(trials)         # counts the number of successes
    
    if s == x:
        j = j + 1           # counts the number of trials with the desired successes
        
probability = j / N
print(probability)