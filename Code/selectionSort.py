import random
import datetime
def selectionSort(list):
    d = 1
    l = len(list)
    i = 0
    for d in range(1,l):
        s = d - 1
        for i in range(d-1,l):
            if (list[i]<list[s]):
                s=i
        temp = list[d-1]
        list[d-1] = list[s]
        list[s] = temp
        d = d + 1
    return list
sum = datetime.datetime.now()-datetime.datetime.now()
print "start."
for j in range(0,10):
    a=[]
    for i in range(0,10000):
        a.append(int(random.random()*1000))
    print "Unsorted:",a
    time1= datetime.datetime.now()
    selectionSort(a)
    sum = sum + (datetime.datetime.now()-time1)
    print "Sorted  :",a
print sum, "for ten iterations"
