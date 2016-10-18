a = [1, 2, 5, 10, 255, 3]
sum = 0.0
i = 0
for number in a:
    i=i+1
    sum = sum + int(number)
    avg = sum/i
print "Sum of elements in a:",sum
print "Average of elements in a:",avg
