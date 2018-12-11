#Exercise 1
L = list(range(21, 40))
print(L)

even= L[1::2]
print(even)

o = []
for x in range(21, 40):
    if (x%3==0):
        o.append(str(x))
print (','.join(o))
	
#Exercise 2
print(L[-2:])

#Exercise 3 What's wrong with the following piece of code? Fix it and modify the code in order to have it work AND to have "<i> is in the list" printed at least once
L = ['1', '2', '3']
for i in range(10):   
    if str(i) in L:
        print("i is in the list")
    else:
        print("i not found") 

#Exercise 4 Read the first line from the sprot_prot.fasta file Split the line using 'OS=' as delimiter and print the second element of the resulting list
fast = open('sprot_prot.fasta','r')
fast_2=fast.readline()
print(fast_2)

half_string=fast_2.split('OS=')[-1:]
print(half_string)

#Exercise 5 Split the second element of the list of Exercise 4 using blanks as separators, concatenate the first and the second elements and print the resulting string
#resulting_string= str(half_string).strip('[]')     #eliminating the brackets from the previous list
#resulting_string= resulting_string.split(' ') #splitting the resulting string
#print (resulting_string[0] + resulting_string[1])

#Exercise 6 reverse the string 'asor rosa'
#str1 = 'asor rosa'
#print(str1[::-1])

#Exercise 7 Sort the following list: L = [1, 7, 3, 9]
#L = [1,7,3,9]
#L.sort()
#print(L)

#Exercise 8 Create a new sorted list from L = [1, 7, 3, 9] without modifying L
#l2= []
#if i in L:
#	l2 = L
#	l2.sort()
#	print(l2)

#Exercise 9 Write to a file the following 2 x 2 table:
# 2 4
# 3 6
tab= '2\t4\n3\t6'
print(tab)
F = open('table.txt','w')
F.write('2\t4\n3\t6')
