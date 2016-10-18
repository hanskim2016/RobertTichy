def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def multiply(x,y):
    result = 0
    # is this recursion?
    for i in range(y):
        result = add(result,x)
    return result
def division(x,y):
    #easy to understand, subtract until what is left is smaller
    #than what we are dividing by
    remainder = x
    quotient = 0
    while remainder >= y:
        quotient += 1
        remainder = sub(remainder,y)
    return (quotient, remainder)
def factorial(n):
    # very easy to understand, straightforward
    if sub(n,1) > 0:
        return multiply(n,factorial(sub(n,1)))
    else:
        return 1
def power(x,y):
    result = 1
    for i in range(y):
        result = multiply(x,result)
    return result
print multiply(3,5)
print multiply2(3,5)
# division(37,4)
# print factorial(6)
# power(2,10)
