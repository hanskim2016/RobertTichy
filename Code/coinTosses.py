import random
i = 0
h = ['heads','tails']
heads = 0
for i in range(0,5000):
    f = int(round(random.random()))
    if (f == 1):
        heads = heads + 1
    s= 'Attempt #{0}:Throwing a coin... Its {1}.'.format(i+1,h[f])
    s = s + '  Got {0} heads and {1} tails so far.'.format(heads,i-heads+1)
    print s
