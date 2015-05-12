"""
FizzBuzz Python script
@author Alan Fluder
"""
userNumber = input("Enter your number: ")
while (userNumber >= 107):
    userNumber = input("Number must be less than 107. \nEnter your number: ")
for num in range(1,userNumber+1):
    if (num%3 == 0 and num%5 == 0):
        print "FizzBuzz"
    elif (num%3 == 0):
        print "Fizz"
    elif (num%5 == 0):
        print "Buzz"
    else:
        print num
        
        
        

