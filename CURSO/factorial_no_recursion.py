def factorial(n):
    if n < 1:
        return None
    if n < 2:
        return 1
    
    init = 1
    
    for i in range(2, n  +  1 ):
        init *= i
    return init
        
for num in range(0, 5):
    print(num, factorial(num), sep = " => ")
    

"""
Output: 
0 => None
1 => 1
2 => 2
3 => 6
4 => 24
"""