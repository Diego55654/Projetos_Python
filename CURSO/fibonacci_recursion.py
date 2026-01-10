def fib(num):
    if num < 1:
        return None
    if num < 3:
        return 1
    
    return fib(num - 1) + fib(num - 2)

for n in range (0 , 10):
    print(n, fib(n) , sep = " => ")

"""
Output:
0 => None
1 => 1
2 => 1
3 => 2
4 => 3
5 => 5
6 => 8
7 => 13
8 => 21
9 => 34
"""
