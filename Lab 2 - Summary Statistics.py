# Tutorial on determining summary statistics using Python
# Kacy Rowe 
# 1/29/18 
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
print("The mean of the numbers you entered is ", mean)

# Calculate the median

numbers.sort()
# Or just type numbers in the console to see this
print(numbers)

if N % 2 == 0:
    mOne = N/2
    mTwo = (N/2) + 1
    
    # Positions
    mOne = int(mOne) - 1
    mTwo = int(mTwo) - 1
    
    median = (numbers[mOne] + numbers[mTwo]) / 2
    print("The median of the numbers you entered is ", median)
    
else:
    m = (N + 1) / 2

