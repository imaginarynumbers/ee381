# Tutorial on determining summary statistics using Python
# Kacy Rowe 
# 1/30/18 
#

numbers = [ ]
# User inputs data
while True:
    
    try:
        n = int(input('Enter a number. To stop, enter the letter s. '))
        #numbers[0] = n
        numbers.append(n)
    except ValueError:
        break
            
            
# Mean calculation
s = sum(numbers)
N = len(numbers)
# Calculate the mean.
mean = s/N


# Calculate the median

numbers.sort()
# Or just type numbers in the console to see this
print('Sorted numbers')
print(numbers)
print("The mean of the numbers you entered is ", mean)

if N % 2 == 0:
    # For an even number of datums
    mOne = N/2
    mTwo = (N/2) + 1
    
    # Positions
    mOne = int(mOne) - 1
    mTwo = int(mTwo) - 1
    
    median = (numbers[mOne] + numbers[mTwo]) / 2
    print("The median of the numbers you entered is ", median)
    
else:
    # For an odd number of datums
    m = (N + 1) / 2
    m = int(m) - 1
    median = numbers[m]

print('The median of the numbers you enters is ' , median)


# Calculate the mode.

from collections import Counter

c = Counter(numbers)

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
    
# Calculate the Standard Deviation
    
import math

a = 0

for x in numbers:
    #** = exponent
    y = (x - mean) ** 2
    a = a + y
sigma = math.sqrt(a/N)

print('The standard deviation is ', sigma)