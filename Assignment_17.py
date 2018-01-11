list1=[0,2,3,4,10,9,7]
small=list1[0]
big=list1[1]
for i in range(len(list1)):
	if (small > list1[i]):
		small=list1[i]
	elif(big<list1[i]):
		big=list1[i]
print "small element in list is",small
print "small element in list is",big