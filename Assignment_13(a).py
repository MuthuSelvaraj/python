num1=input("enter num1\n")
print "\n"
num2=input("enter num2")
print "\n"
num3=input("enter num3")
print "\n"
num4=input("enter num4")
print "\n"
if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
   
 largest = num1

elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
  
 largest = num2

elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
  
 largest = num3

else:
  
 largest = num4


print "The largest number between",num1,num2,num3,num4,"is",largest