
upper = int(input("Enter upper range: "))  
  
for num in range(1,upper + 1):  
   if num > 1: 
       count = 2 
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
	   count=count+1
       
       if(num == count):  
           print(num)  