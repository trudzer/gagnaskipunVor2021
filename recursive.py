#example function--------------------------------------------------------------------------

def example_func(n):
    return example_func_helper(0,n)

def example_func_helper(i, n):
    if i > n:
        return 0
    print(i, end=" ")
    return i + example_func_helper(i+1, n)
print("Example: ", end="")
print(example_func(5))

#power function----------------------------------------------------------------------------

def power_func(base, exp):
    if exp == 0:
        return 1
    return base * power_func(base, exp-1)
print("Power: ", end="")
print(power_func(4,2))

#multiply function------------------------------------------------------------------------

def multi_func(a,b):
    neg_counter = 0
    if a < 0:
        neg_counter += 1
    if b < 0:
        neg_counter += 1
    if neg_counter == 1:
        return -multi_func_helper(abs(a), abs(b))
    else:
        return multi_func_helper(abs(a), abs(b))

def multi_func_helper(a,b):
    if a == 0:
        return 0
    return b + multi_func(a-1, b)
print("Mutliply: ",end="")
print(multi_func(4,4))

#factorial function------------------------------------------------------------------------

def factorial_func(n):
    if n == 0:
        return 1
    return n * factorial_func(n-1)
print("Factorial: ",end="")
print(factorial_func(5))

#natural numbers function-----------------------------------------------------------------

def natural_func(n):
    if n == 0:
        return
    natural_func(n-1)
    print(n, end=" ")
print("Natural numbers: ",end="")
natural_func(5)

#sum of digits function--------------------------------------------------------------------

def sum_of_digits_func(x):
    if x < 10:
        return x
    return sum_of_digits_func(x % 10) + sum_of_digits_func(x // 10)

print("\nSum of digits: ",end="")
print(sum_of_digits_func(254))

#fibonacci function-----------------------------------------------------------------------

def fib_func(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_helper_func(n, 0, 1, 2)

def fib_helper_func(n, a, b, i):
    if i == n:
        return a + b
    temp = b
    b = b + a
    a = temp
    return fib_helper_func(n, a, b, i+1)

print("Fibonacci: ",end="")
print(fib_func(20))

#------------------------------------------------------------------------------------------
