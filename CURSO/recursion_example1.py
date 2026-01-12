def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(3))

"""
Thinking model:
f(3)
= 3 + f(2)
= 3 + (2 + f(1))
= 3 + (2 + (1 + f(0)))
= 3 + 2 + 1 + 0
= 6
"""
