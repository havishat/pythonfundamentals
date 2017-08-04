import random

def grade(reps):
    print "Scores and Grades"
    for x in range(0, reps):
        score = random.randint(60, 101)
        if score >= 60 and score <=69:
            print "Score:", score, "; Grade - D"
        elif score >= 70 and score <=79:
            print "Score:", score, "; Grade - C"
        elif score >= 80 and score <=89:
            print "Score:", score, "; Grade -B"
        elif score >= 90 and score <=100:
            print "Score:", score, "; Grade - A"
        else:
            print "you failed"
    print "End of the program. Bye!"

    
grade(1)

        