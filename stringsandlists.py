#def findreplace(): 
words = "It's thanksgiving day. It's my birthday,too!"
Index = words.find('day')
replace = words.replace('day', 'month')
print Index
print replace
#findreplace()

#def minmax():
x = [2,54,-2,7,12,98]
print "min:", min(x)
print "max:", max(x)
#minmax()

def firstlast(list):
#x = ["hello",2,54,-2,7,12,98,"world"]
    newlist = []
    newlist.append(list[0])
    newlist.append(list[len(list)-1])
    print newlist
firstlast(["world",2,3,4,"hello"])

def newList(x):
    x.sort()
    print x
    first = x[0:len(x)/2]
    print first
    second = x[len(x)/2:]
    print second
    second.insert(0,first)
    print second 
newList([19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6])
