num1=input("enter num1")
print "\n"
for i in range(2,num1):
    if (num1 % i ==0):
        print "The number ",num1 ,"is not prime"
        break
else:
         print "The number ",num1 ,"is  prime"
         