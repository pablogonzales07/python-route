import time

def factorial(n):
    response = 1
    while n>1:
        response *= n
        n -= 1
    
    return response

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)


if __name__ == '__main__':
    n = 1000

    beggin = time.time()
    print(factorial(n))
    end = time.time()
    print(final - comienzo)
    
    
