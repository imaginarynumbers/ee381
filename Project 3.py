#Kacy Rowe
#Project 3
import math
from random import *
import random

def choose(num1, num2):
    factorial = math.factorial
    result = factorial(num1) / (factorial(num2) * factorial(num1-num2))
    return result
  
def part_one_two():
    n = 5
    trials = [0]
    trials = trials*n
    trials_tracker = [0]
    trials_tracker = trials_tracker*6
    attempts = 1000
    probability = 0.7
    accumulator = 0
    successes = 3
    accumulator = 1
    for i in range(attempts):
        for j in range(n):
            x = random.uniform(0,1)
            if x < probability:
                trials[j] = 1
            else:
                trials[j] = 0
        sum_of_trials = sum(trials)
        trials_tracker[sum_of_trials] += 1
        if sum_of_trials == successes:
            accumulator = accumulator + 1
    
    final_prob = choose(5,3)*probability**(3)*(1-probability)**(5-3)
    expected = 0 * trials_tracker[0] + 1 * trials_tracker[1] + 2 * trials_tracker[2] + 3 * trials_tracker[3] + 4 * trials_tracker[4] + 5 * trials_tracker[5]
    #final_prob = accumulator / attempts
    print(trials_tracker)
    print('probability of exactly 3 is:', format(final_prob, '.5f'))
    print('mu =', 5*probability)
    print('expected value of the random variable:', expected)
    print('The expected value =', trials_tracker[4]/attempts)

def part_three(input_success,input_probability,input_trials,in_list):
    n = input_trials
    trials = in_list
    trials_tracker = [0]
    trials_tracker = trials_tracker*input_success
    attempts = input_trials
    probability = input_probability
    accumulator = 0
    successes = input_success
    accumulator = 1
    for i in range(attempts):
        for j in range(n):
            x = random.choice(trials)
            if x < probability:
                trials[j] = 1
            else:
                trials[j] = 0
        sum_of_trials = sum(trials)
        trials_tracker[sum_of_trials] += 1
        if sum_of_trials == successes:
            accumulator = accumulator + 1
    
    final_prob = choose(input_trials,successes)*probability**(successes)*(1-probability)**(input_trials-successes)
    expected = 0 * trials_tracker[0] + 1 * trials_tracker[1] + 2 * trials_tracker[2] + 3 * trials_tracker[3] + 4 * trials_tracker[4] + 5 * trials_tracker[5]
    #final_prob = accumulator / attempts
    print(trials_tracker)
    print('probability of exactly 3 is:', format(final_prob, '.5f'))
    print('expected value of the random variable:', expected)
    print('The expected value =', trials_tracker[4]/attempts)

user_input_list = []
print('Binomial Distribution Experiment')
part_one_two()
print('Begin Part III')
input_probability =  float(input('Input the probability of success\n'))
input_trials = int(input('Input the number of trials\n'))
input_success = int(input('Input the number of successes\n'))
print('Input the range of values for the number of successes (-1 to quit)')
input_string = input('Enter a comma delimited range of values for the number of successes.\n')
string_li = input_string.split(",")
for element in string_li:
    user_input_list.append(int(element))
part_three(input_success,input_probability,input_trials,user_input_list)
# def part_three(input_success,input_probability,input_trials,in_list):


#PART ONE
#Simulation 1. Write a Python program to simulate the specific problem above. 
#In this program import and use the Python random number generator. 
#You, arguably, need to consider the finite number of Bernoulli trials in the problem 
#and the number of successes in the finite number of Bernoulli trials.