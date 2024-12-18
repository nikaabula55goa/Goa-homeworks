def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

# Examples:
print(get_sum(1, 0))  
print(get_sum(1, 2))  
print(get_sum(0, 1))  
print(get_sum(1, 1))  
print(get_sum(-1, 0)) 
print(get_sum(-1, 2)) 