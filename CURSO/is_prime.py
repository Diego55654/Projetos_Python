def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i):
        print(i, end=" ")

#Output : 2 3 5 7 11 13 17 19 


