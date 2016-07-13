"""
Discount Offers problem from:
https://www.codeeval.com/public_sc/48/
Assignment Problem, best algorithm to use is Munkres/Hungarian with running time of O(n^3).
Program accepts path to file as command line argument, or defaults to included in.txt in the event of none specified.
By: Logan Tassie
May 5th, 2016

Using Munkres module for Munkres/Hungarian algorithm downloaded from:
https://pypi.python.org/pypi/munkres
(Licence included in folder)

"""

from munkres import Munkres, print_matrix
import sys

def isVowel(c):
	if c in ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'):
		return True
	return False
	
def isConsonant(c):
	if c.isalpha() and not isVowel(c):
		return True
	return False
	
def hasSharedFactor(a, b):
	limit = min(a, b)
	for i in range(2, limit + 1):
		if (a%i == 0) and (b%i == 0):
			return True
	return False

if len(sys.argv) > 1:
	infile = sys.argv[1]
else:
	infile = 'in.txt'
names = []
products = []
for line in open(infile, 'r'):
	max = 0 #Used later to revert score values so Hungarian-Algorithm library can work on it.
	matrix = [] #Matrix (Nested List in Python) to contain a suitability score for every permutation of customer/product.
	#Split lines into names and products based on the semicolon, then split those strings into lists of names and products based on the commas.
	names, products = line.rsplit(';')[0].rsplit(','), line.rsplit(';')[1].rsplit(',')
	#Then strip newline character (\n) from the last entry.
	products[-1] = products[-1].strip('\n')
	for customer in names:
		suitability = [] #List of a single customer's suitability score for each product.
		#Problem states for each *letter*, not character.
		custlen = sum(c.isalpha() for c in customer)
		for item in products:
			itemlen = sum(c.isalpha() for c in item)
			matchscore = 0
			if itemlen %2 == 0:
				matchscore = sum(isVowel(c) for c in customer)*1.5
			else:
				matchscore = sum(isConsonant(c) for c in customer)
			if hasSharedFactor(custlen, itemlen):
				matchscore *= 1.5
			suitability.append(matchscore)
			if matchscore > max:
				max = matchscore
		matrix.append(suitability)
	
	####
	#Remainder of the code is borrowed from https://pypi.python.org/pypi/munkres with minor modifications and comments from myself.
	#Munkres works as a minimization problem, whereas this is a maximization problem. Solution is to reverse matrix beforehand, so maximum values become minimum.
	####
	cost_matrix = []
	for row in matrix:
		cost_row = []
		for col in row:
			cost_row += [max - col]
		cost_matrix += [cost_row]
	#Run library
	m = Munkres()
	indexes = m.compute(cost_matrix)
	
	#Calculate total
	total = 0
	for row, column in indexes:
		value = matrix[row][column]
		total += value
	print(total)
