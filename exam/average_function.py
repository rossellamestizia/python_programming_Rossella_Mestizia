# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

def elementi():
	vector = vectors(10)
	a = average(vector)
	print("This is input list: %s" %n)
	print("This is average: %s" % a)

vect = []
def vectors(vector):
	for i in range(0,10):
		vec = input("please type input #%s: " % int(i+1))
		vect.append(i, vec)
		return(vect)

def average(vec):
	return(sum(vec)/float(len(vec)))
	print(average)
#compute the average of the numbers

