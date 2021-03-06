"""
https://www.reddit.com/r/dailyprogrammer/comments/4fc896/20160418_challenge_263_easy_calculating_shannon/
####################################################################################
####################################################################################
[2016-04-18] Challenge #263 [Easy] Calculating Shannon Entropy of a String
####################################################################################
####################################################################################
Description
####################################################################################

Shannon entropy was introduced by Claude E. Shannon in his 1948 paper "A Mathematical Theory of Communication". Somewhat related to the physical and chemical concept entropy, the Shannon entropy measures the uncertainty associated with a random variable, i.e. the expected value of the information in the message (in classical informatics it is measured in bits). This is a key concept in information theory and has consequences for things like compression, cryptography and privacy, and more.
The Shannon entropy H of input sequence X is calculated as -1 times the sum of the frequency of the symbol i times the log base 2 of the frequency:
            n
            _   count(i)          count(i)
H(X) = -1 * >   --------- * log  (--------)
            -       N          2      N
            i=1
(That funny thing is the summation for i=1 to n. I didn't see a good way to do this in Reddit's markup so I did some crude ASCII art.)
For more, see Wikipedia for Entropy in information theory).

####################################################################################
Input Description
####################################################################################

You'll be given a string, one per line, for which you should calculate the Shannon entropy. Examples:
1223334444
Hello, world!

####################################################################################
Output Description
####################################################################################

Your program should emit the calculated entropy values for the strings to at least five decimal places. Examples:
1.84644
3.18083

####################################################################################
Challenge Input
####################################################################################

122333444455555666666777777788888888
563881467447538846567288767728553786
https://www.reddit.com/r/dailyprogrammer
int main(int argc, char *argv[])

####################################################################################
Challenge Output
####################################################################################

2.794208683
2.794208683
4.056198332
3.866729296

"""

import sys
import math

class ShannonEntropyCalc (object):

	def __init__(self):
		self._infile = 'in.txt'
		self._outfile = 'out.txt'
		self._loopnumbers = 0

	def main(self):
		for line in open(self._infile, 'r'):
			line = line.replace('\n', '')
			entropy = self.CalculateEntropy(line)
			output = round(entropy, 4)
			print(entropy)
			print(self._loopnumbers)
			
	def CalculateEntropy(self, line):
		entropy = 0
		counted = ''
		linelength = len(line)
		for i, c in enumerate(line):
			if c not in counted:
				count = self.CountCharacter(i, c, line)
				entropy += (count/linelength)*(math.log2(count/linelength))
				counted += c
		return(-entropy)
		
	def CountCharacter(self, i, c, line):
		count = 0
		################################################################# Method 1 branch
		while i < len(line):
			self._loopnumbers += 1
			if line[i] == c:
				count += 1
			i += 1
		################################################################# Method 2 branch
		#for ch in line:
		#	self._loopnumbers += 1
		#	if ch == c:
		#		count += 1
		################################################################# End branch
		return count

calc = ShannonEntropyCalc()
calc.main()






























