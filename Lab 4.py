# Random Number Generator

# Below are fixed values for the generator formula

N = 10000 # norm
A = 4857  # adder
M = 8601  #multipier

a = 0 # accumulator

S = int(input("Enter the non-negative integer of the seed. "))

k = int(input("Enter the number of random numbers you want. "))

for i in range(1,k+1):
    S = (M * S + A) % N
    r = S/N # Random numbers on [0,1)
    print(format('%.4f'%r))
    
    a = a + r # accumulator
    
average = a/k

    