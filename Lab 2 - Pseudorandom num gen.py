# Pseudorandom number generator
# Kacy Rowe Lab 2 
# 1/24/18 
#
# This program is an exploration of the pseudorandom number generator
# 
#import libraries
import math

# Below the parameters in the formula are assigned their values
M = 41
A = 31
N = 100


# Below is a prompt for the user to enter their seed.
S = int(input("Enter the value of your seed. ")) # cast as int

for k in range(50): #k is the target variable
#Below is the formula
    S = (M * S + A) % N
    r = S/N
    print('%.3f'%r)
    
    number = math.floor(r * 6 + 1) #round down, linear transformation
    print(number)
