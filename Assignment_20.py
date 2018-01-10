r=input('Enter the fibonacci range\n')
a=0
b=1
print a
print b
for i in range(1,r-1):
        c=a+b
        a=b
        b=c
        print c
