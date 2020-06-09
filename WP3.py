def are_all_condition_true(conditions):
    for i in conditions:
        if(i==False):
            return False
    return True

iconditions={True,True,True}
print(are_all_condition_true(iconditions))