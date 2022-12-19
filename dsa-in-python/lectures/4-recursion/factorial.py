def factorialRecursive(n): 
    if n == 1: 
        return n 
    return n * factorialRecursive(n - 1)

def factorialIterative(n): 
    ret = n
    while n > 1: 
        ret *= n - 1
        n -= 1

    return ret


assert(factorialRecursive(1) == 1)
assert(factorialRecursive(2) == 2)
assert(factorialRecursive(3) == 6)
assert(factorialRecursive(4) == 24)


assert(factorialIterative(1) == 1)
assert(factorialIterative(2) == 2)
assert(factorialIterative(3) == 6)
assert(factorialIterative(4) == 24)