#Odd/Even
def odd_even():
    for count in range(0,2001):
        if(count%2==0):
            print "Number is", count,  "This is an even number"
        else :
            print "Number is", count, "This is an odd number"
odd_even()

# Multiply:
def multiply(arr,num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr
num_arr = [3,6,8,10,67]
print multiply(num_arr,5)

# Hacker Challenge
def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
