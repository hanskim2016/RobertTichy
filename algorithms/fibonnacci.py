def fib(a,b,lvl):
    lvl +=1
    if lvl<8:
        return fib(b,a+b,lvl)
    else:
        return a+b

print fib(0,3,0)
