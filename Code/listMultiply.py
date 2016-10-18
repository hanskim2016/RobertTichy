def listMultiply(list,factor):
    list2=[]
    for each in list:
        list2.append(each*factor)
    return list2
a = [2,4,10,16]
b = listMultiply(a,5)
print b
