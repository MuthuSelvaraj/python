listA=[1,2,3,4,5,6,7,8,9,10]
listB=['abi','balu','chrish','dheep','muthu','kannan','guru','harsha','john','peter']
for i in range(len(listB)):
	print listB[i]
print "\n"
index=input('enter the index\n')
print "the corresponding emp name is", listB[index-1], "and the id of employee is",listA[index-1]
listC=listB[3:9]
print "Names from 4th to 9th is\n"
for i in range(len(listC)):
	print listC[i]
listD=listB[2:10]
print "Names from 3rd to end of the list is\n"
for i in range(len(listD)):
	print listD[i]
rep=input('Specify how many times list elements will be repeated\n')
print "After repeat the elements in the list"
print listA*rep
print listB*rep
print "Concatenation of the 2 list is\n",listA+listB
print "\n"
print "elements from two lists are printed side by side"
for i in range(len(listA)):
	print "Empid is",listA[i],"Name is",listB[i]
