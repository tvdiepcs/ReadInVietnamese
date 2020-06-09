def is_a_condition_true(conditions):
    for i in conditions:
        if(i):
            return True
    return False

iconditions={True, False, False}
print(is_a_condition_true(iconditions))