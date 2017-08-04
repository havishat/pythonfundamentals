



# num = int(input("Enter a number: "))
for num in range(2,37):
#for count in range (0,num):
# prime numbers are greater than 1
    if num > 1:
    # check for factors 
        prime = True
        for i in range(2,num):
           # print i
            if (num % i) == 0:
                prime = False
               # print(num,"FooBar")
                break
        if prime: 
            print(num,"Foo") # If it is a prime number print "Foo"
        x = num**.5
        y = int(x)
        if x**2 == y**2:
            square = True
            print "Bar ", num #If it is a perfect square print "Bar"
        elif prime == False :
            print "FooBar", num
        

    

