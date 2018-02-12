'''
Find the highest coin in the pool who's value is less than the target amount
subtract one of those coins in the pool and subtract its value from the target amount
continue until the target amount is 0 (returns true or the list of required coins) or until there is no coin available with a value less than the target (returns false)

'''
 
def exact_change(target_amount, values, start_index=0, ret=None):
    if ret == None:
        ret = [0] * len(values)

    for i in range(start_index, len(values)): # start at start_index
        #if L[i] == 0:
        #    continue
        if values[i] == target_amount:
            ret[i] += 1
            return ret
        elif values[i] < target_amount:  
            ret[i] += 1
            result = exact_change(target_amount-values[i], values, i, ret) # pass i as start_index
            if result:     # check the result to make sure it was successful before returning
                return result
            #L[i] += 1      # backtrack if it was not
            ret[i] -= 1
    else:
        return False   # None might be a more natural value to return here

print(exact_change(332, [25, 10, 5, 1]))