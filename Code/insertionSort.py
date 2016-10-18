import random
import datetime
def insertionSort(list):
    last = len(list)
    sorted = 0
    if (len(list) <= 1):
        return
    consider = 1
    while (sorted<last-1):
        if (list[consider]<list[sorted]):
            temp=list[consider]
            i=sorted
            while (list[i] > temp and i>=0):
                list[i+1] = list[i]
                list[i]=temp
                i=i-1
        sorted=sorted+1
        consider=sorted+1
sum = datetime.datetime.now()-datetime.datetime.now()
print "start."
for j in range(0,10):
    a=[]
    for i in range(0,10000):
        a.append(int(random.random()*1000))
    print "Unsorted:",a
    time1= datetime.datetime.now()
    insertionSort(a)
    sum = sum + (datetime.datetime.now()-time1)
    print "Sorted  :",a
print sum, "for ten iterations"
