def gradeIt(score):
    if (score >= 90):
        return "\r\r;  That's an 'A'."
    elif (score >= 80):
        return "  That's a 'B'."
    elif (score >= 70):
        return "  That's a 'C'."
    elif (score >= 60):
        return "  That's a 'D'."
    else:
        return "  That's an 'F'."
score =0
i = 0
print "Scores and grades."
for i in range(0,10):
    score = int(raw_input("Score:"))
    print gradeIt(score)
print "End of the program.  Bye!"
