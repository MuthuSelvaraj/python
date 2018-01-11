import math
list1=[]

a=0

less=0

eq=0
more=0
print "enter the 10 numbers"

for i in range(10):
   
  num=input('')
  
  a=a+num
    
  list1.append(num)

avg=a/float(10)

print "Average of 10 number is",avg

avg1=round(avg,0)

for i in range(len(list1)):
    
  if( avg1 == list1[i]):
        
    eq=eq+1
    
  elif(avg1 > list1[i]):

    more=more+1
   
  else:
        
    less=less+1

print "Number of elements equal to avg is",eq

print "Number of elements less than avg is",more

print "Number of elements more than avg is",less
