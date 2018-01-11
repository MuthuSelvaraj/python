import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])  
d = int(sys.argv[4])
e = int(sys.argv[5])  

print a
print b
print c
print d
print e
largest=0
if (a>=b and a>=c):
    largest=a
elif(b>=c and b>=a):
    largest=b
else:
    largest=c
print "The biggest of first three numbers from command line ",a,b,c, "is ",largest    
