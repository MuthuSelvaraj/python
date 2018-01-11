listA=['john','peter','mark','rock','kane']
ele=raw_input('Enter the Element you want to search in the list\n')
if(ele in listA):
	print "The specified element is exist in the list(using membership operator)"
else:
	print "The specified element is not exist in the list(using membership operator)"
for i in range(len(listA)):
	if(listA[i]==ele):
		flag=1
		#print "The specified element is exist in the list(not using membership operator)"
	else:
		flag=0
		#print "The specified element is exist in the list(not using membership operator)"
if(flag==1):
	print "The specified element is exist in the list(not using membership operator)"
else:
	print "The specified element is exist in the list(not using membership operator)"