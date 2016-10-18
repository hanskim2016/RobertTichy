def printStars( n ):
    s = ""
    if (type(n) == int):
        for i in range(0,n):
            s = s + "*"
        return s
    elif (type(n) == str):
        for i in range(0,len(n)):
            s = s + n[0].lower()
        return s
def drawStars2(array):
    for each in array:
        print printStars(each)
a = [3,'Tom','Dick',12,'Harry']
drawStars2(a)
