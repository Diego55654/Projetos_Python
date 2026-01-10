def factorial(n):
    if n < 1:
        return None
    if n < 2:
        return 1
    
    return n * factorial(n - 1)
    
for n in range(1, 10):
    print(n, factorial(n), sep = " => ")

"""
Output: 
0 => None
1 => 1
2 => 2
3 => 6
4 => 24
"""













