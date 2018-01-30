def helper(s):
    if not s:
        return [[]]
    results = []
    for i in range(len(s), 0, -1):
        sub = s[:i]
        if sub == sub[::-1]:
            for rest in helper(s[i:]):
                results.append([sub] + rest)
    return results

def palindromic_substrings(s):
    results=helper(s)

    flat_list = [item for sublist in results for item in sublist]
    
    print len(flat_list)
    #print flat_list 
    res = set(flat_list)
    #print(len(res))
    return len(res)
    #return []

print(palindromic_substrings("aabaa"))