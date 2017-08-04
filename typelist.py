#myNumsList = [1,3,'a','asfdlfa','afdf', 1, 2, 'sfs']
#myNumsList = [2,3,1,7,4,12]
#myNumsList = ['magical','unicorns']
myNumsList = ['magical unicorns',19,'hello',98.98,'world']

count = 0
sum1 = 0
list1 = []
while count < len(myNumsList):
    for element in myNumsList:
        if isinstance(element, int) or isinstance(element, float):
            sum1 += element
            count = count + 1
        elif isinstance(element, str):
            list1.append(element)
            count = count + 1
        
    if sum1 and list1 :
        print "The array you entered is of mixed type"
        print "string: ", ' '.join(list1)
        print "Sum:", sum1
    elif list1 :
        print "The array you entered is of string type"
        print "string: ", ' '.join(list1)
    else:
        print "The array you entered is of integer type"
        print "Sum:", sum1
