# Kacy Rowe
# Part 1
# Bernoulli Trials

import random
main_list = []
suc_fail_list = []
input_choice = 0
number_of_successes = 0
input_number = int(input('Specify the number of trials\n'))
input_success = int(input('Input the number of heads (successes)\n'))
for i in range(0,input_number):
    main_list.append(random.randint(0,1))
for k in range(0,len(main_list)):
    if main_list[k] == 0:
        suc_fail_list.append('F')
        number_of_successes += 1
    else:
        suc_fail_list.append('S')
    
difference_of_successes = input_success - number_of_successes
print(suc_fail_list,'\nThe number of actual successes is: ', number_of_successes)
print('\nThe difference is: ', difference_of_successes)
percentage = difference_of_successes * 100 / number_of_successes
print((format(percentage, '.2f')),'%')