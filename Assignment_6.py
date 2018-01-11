str1=raw_input("enter the string")

str2=raw_input("enter the string")

print "\n"

print "print each character seperately"

for i in range(len(str1)):
   
   print str1[i]

str3=str1[1:4]

print "The substring is ",str3

print "100 times of the string is",str3*100

print "concat of ",str1,str2, "using + is",str1+str2