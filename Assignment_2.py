num1=input("enter num1")
print "\n"
num2=input("enter num2")
print "\n"
num3=input("enter num3")
print "\n"
if (num1 >= num2) and (num1 >= num3):
   
 largest = num1

elif (num2 >= num1) and (num2 >= num3):
  
 largest = num2

else:
  
 largest = num3


print "The largest number between",num1,",",num2,"and",num3,"is",largest