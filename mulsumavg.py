#multiples part 1
for count in range (1,1000):
    if count%2==1:
        print count

#multiples part 2
for count in range (5,1000000):
    if count%5==0:
        print count

#sum list
def sumlist(a):
    b = sum(a)
    print b
sumlist([1,2,5,10,255,3])

#average list
def avglist(a):
    c = len(a)
    b = sum(a)/len(a)
    print b
avglist([1,2,5,10,255,3])
        
