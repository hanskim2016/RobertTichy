def printStars( n ):
    s = ""
    for i in range(0,n):
        s = s + "*"
    return s
def drawStars(array):
    print array
    for each in array:
        print printStars(int(each))
        # print p
a = [3,5,7,1]
drawStars(a)
