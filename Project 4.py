# Kacy Rowe
# Project 4
# EE 381

# Imports
import math
import matplotlib.pyplot as plt
import numpy as np

#There is an established system in use that works 50% of the time. 
#A new system is available and it is argued that the new system is an improvement 
#with a probability that it works exceeding 50%. Both the old and the new systems 
#are expensive to run and are time consuming to operate. Thus, only a small 
#number of trials can be performed. Since there will be a finite number 
#of trails, the probability in each trial is constant, there are two 
#outcomes, and each trial is independent we are considering a Binomial R.V.

# Global Items
trials = 18
probability = 0.5
range_list = np.arange(0.50,1.05,0.05)

# Formula Function
def choose(num1, num2):
    factorial = math.factorial
    return factorial(num1) / factorial(num2) / factorial(num1-num2)

def part_one():
# Binomial Distribution
  list_factorials = []    #to hold the calculated trials
  for i in range (0,trials + 1):
    list_factorials.append(choose(18,i)*(probability**(i))*((probability)**(18-i)))
  # Print the graph
  N = len(list_factorials)
  x = range(N)
  width = 1/1.5
  plt.bar(x, list_factorials, width, color = "blue")
  plt.show()

def part_two():
# Critical Values
    sum_list = []
    for i in range (0,trials + 1):
        critical_values = []
        for j in range(i,trials + 1):
            critical_values.append(choose(18,i)*(probability**(i))*((probability)**(18-i)))
        # Sum up the Critical Values
        sum_list.append(sum(critical_values))
    
    for k in range(0, len(sum_list)):
        print(k, '\t', format(sum_list[k], '.6f'))
    print (critical_values)
 
def part_three():
# Graph Test
    critical_value = 13
    for i in range_list:
        graph_list = []
        for j in range (0,19):
            graph_list.append(choose(18,j) * (i**(j)) * (1-i) ** (18-j))
        # Print multiple graphs
        N = len(graph_list)
        x = range(N)
        width = 1/1.5
        plt.bar(x, graph_list, width, color = "blue")
        plt.show()
# Beta Test
# 1 - beta
    beta_list = []
    for i in range_list:
        beta = 0
        for j in range (0,critical_value):
            beta += choose(18,j) * (i**(j)) * (1-i) ** (18-j)
        beta_list.append(1-beta)
    # Print the graph
    N = len(beta_list)
    x = range(N)
    width = 1/1.5
    plt.plot(range_list, beta_list, width, color = "blue")
    plt.xticks(range_list)
    plt.show()
        

# Main 
print('Hypothesis: H0 = 1/2(50%), H1 > 1/2(50%)')
part_one()
part_two()
part_three()