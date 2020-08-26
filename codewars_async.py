def is_prime(num: int):
    import math
    if num <= 1: return False
    for x in range(2, int(math.sqrt(num)+1)):
        if num % x == 0:
            return False
    return True

print(is_prime(20000))