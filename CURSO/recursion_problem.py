def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

"""
a = 25 ; a = 28 and fun(31) ...

31 > 30, so  25 + 28 + 3 = 56
"""

print(fun(25))
print(fun(30))
print(fun(31))