import random
def tossingcoin(reps):
    attempt_count = 1
    head_count = 0
    tail_count = 0
    result = ""
    #result_string_complete = ""

    for x in range(1, reps):
        
        newtoss = random.randint(0,1)
        if newtoss is 1:
            head_count += 1
            result = "Attempt #", attempt_count, ": Throwing a coin... It's a", result, "! ... Got", head_count , "head(s) so far and", tail_count, "tail(s) so far"
        else : 
            tail_count += 1
            result = "tail"
            print "Attempt #",attempt_count,": Throwing a coin... It's a", result, "! ... Got", head_count,  "head(s) so far and", tail_count, "tail(s) so far"
        attempt_count += 1
tossingcoin(6)
