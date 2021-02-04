def power_recur(base, exp):
    if exp == 0:
        return 1
    return base * power_recur(base,exp-1)
    
#print(power_recur(4,4))

def multi_recur(a,b):
    neg_counter = 0
    if a < 0:
        neg_counter += 1
    if b < 0:
        neg_counter += 1
    if neg_counter == 1:
        return -multi_helper(abs(a),abs(b))
    else:
        return multi_helper(abs(a),abs(b))

def multi_helper(a,b):
    if a == 0:
        return 0
    return b + multi_recur(a-1, b)

#print(multi_recur(3, 3))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
#print(factorial(5))

def natural(n):
    if n <= 0:
        return 1
    natural(n-1)
    print(n, end= ' ')
#natural(10)

def sum_of_digits(x):
    if  x < 10:
        return x
    return x%10 + sum_of_digits(x//10)

#print(sum_of_digits(25491))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_helper(n, 0, 1, 2)

def fib_helper(n, a, b, i):
    if i == n:
        return a + b
    temp = b
    b = b + a
    a = temp
    return fib_helper(n, a, b, i+1)

print(fib(3))