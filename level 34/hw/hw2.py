def generate_diagonal(n, l):
   
    from math import comb
    return [comb(n + i, i) for i in range(l)]


print(generate_diagonal(0, 5)) 
print(generate_diagonal(1, 5))  
print(generate_diagonal(2, 5))  
print(generate_diagonal(3, 0))  
