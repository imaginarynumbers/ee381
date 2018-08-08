# Kacy Rowe
# EE 381
# Some of the code used in this project was used from demos in the lab
# Otherwise, everything else was written by me


# Imports
from collections import Counter
import math

# Global items

# Pre-defined set
data_set = [3, 2, 4, 1, 2, 3, 4, 3, 5, 10]
# User defined set
data_set_input = []
# Random defined set
data_set_random = []
seed_set_0to4 = [0, 1, 2, 3, 4]
data_set_prob = []

class ProjectOne:

#------------------------------------------------------------------------------    
    # Part I - Summary Statistics
    def sum_statistics():
        sum = 0
        N = 10
        # Calculate Mean
        for i in (0,len(data_set)-1):
            sum += data_set[i]
        mean = sum / 2
        print('Begin Part I - Summary Statistics.\n')
        print('The mean of the data set is: ',mean)
            
        # Calculate Median
        data_set.sort()
        # Or just type numbers in the console to see this
        print('Sorted numbers')
        print(data_set)
        print("The mean of the numbers you entered is ", mean)
        
        if N % 2 == 0:
            # For an even number of datums
            mid_one = N/2
            mid_two = (N/2) + 1
            
            # Positions
            mid_one = int(mid_one) - 1
            mid_two = int(mid_two) - 1
            
            median = (data_set[mid_one] + data_set[mid_two]) / 2
            print("The median of the numbers you entered is ", median)
    
        else:
            # For an odd number of datums
            m = (N + 1) / 2
            m = int(m) - 1
            median = data_set[m]
            print('The median of the numbers you enters is ' , median)
        
        # Calculate Mode
        # The following has some code given from lab
        c = Counter(data_set)
        
        # Use built-in function
        # The 1 in argument represents the primary, most redundancies?
        mode = c.most_common()
        
        l = [value[1] for value in mode]
        check = max(l)
        if check == 1:
            print('There is no mode.')
            
        else:
            m = mode[0][0]
            print('The mode of the data you entered is ', m)
#------------------------------------------------------------------------------
    # Part II - Random Number Generator
    def random_num_gen():
        # Generate random numbers here
        # The following contains some code given in lab

        # Variables
        M = 10000
        A = 4857
        N = 8601
        S = 5
        random_sum = 0
        random_mean = 0

        random_nums = int(input('\nBegin Part II - Random Number Generator.\nHow many random numbers do you want to generate? '))
        for k in range(0,random_nums):
            #Below is the formula
            S = (M * S + A) % N
            r = S/N
            random_sum += r
            print('%.4f'%r)
            #round down, linear transformation
            #number = math.floor(r * 50 + 1)
            data_set_random.append(r)
        random_mean = random_sum / 100
        print('The mean of the',random_nums,'random numbers:',random_mean)
        
 
#------------------------------------------------------------------------------        
    # Part III - Probability Problem
    def probability():
        # Generate random numbers here
        # The following contains some code given in lab
        # Variables
        M = 89
        A = 31
        N = 99
        S = 8

        experiments = int(input("Begin Part III - Probability Problem.\nEnter the number of experiements to test. "))
        for j in range(experiments*3):
            #Below is the formula
            S = (M * S + A) % N
            r = S/N
            #print('%.4f'%r)
            #round down, linear transformation
            number = math.floor(r * 5 + 1)
            data_set_prob.append(number)
            
        counter = 0
        for k in range(0,experiments):
            print('Experiment #',k+1)
            for l in range(0,3):
              print('Throw number', l+1 , 'landed in cup:', data_set_prob[counter])
              counter += 1
              if l == 2:
                  print
                  print('\n')
              
        
        
       
#------------------------------------------------------------------------------
    # Function calls
    sum_statistics()
    random_num_gen()
    probability()
    