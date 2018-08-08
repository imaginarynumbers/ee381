# Kacy Rowe
# Part II
# Baye's Theorem

# Bayes' Theorem formula
def formula(el1, el2, el3, el4):
    result = ((el2 * el1) / ((el2 * el1) + (el3 * el4)))
    return result

# Lists holding table of information provided
p_of_c_list =  [0.0001, 0.001, 0.001, 0.0001, 0.001]
p_B_C_list =   [0.9, 0.9, 0.9, 0.95, 0.95]
p_B_Cn_list =  [0.001, 0.001, 0.01, 0.001, 0.01]
p_of_Cn_list = [0.9999, 0.999, 0.999, 0.9999, 0.999]
p_C_B_list =  []

# Do the calculations
for i in range(0,5):
    p_C_B_list.append(formula(p_of_c_list[i], p_B_C_list[i], p_B_Cn_list[i], p_of_Cn_list[i]))

# Print the results
print('The results for P(C|B) are: ')
for j in range(0,5):
    print(format(p_C_B_list[j], '.6f'))