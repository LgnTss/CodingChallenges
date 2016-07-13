"""
Challenge: Write a function/method that:
Given strings str1, str2, str3, find whether str3 can be formed by the interleaving of str1 and str2.
For example,
str1 = "aabcc",
str2 = "dbbca",
When str3 = "aadbbcbcac", return true.
When str3 = "aadbbbaccc", return false.
"""


def stringContain(s1, s2, s3):
	if len(s3) > 0:
		if len(s1) > 0 and s1[0] == s3[0]:
				if stringContain(s1[1:], s2, s3[1:]):
					return True
		if len(s2) > 0 and s2[0] == s3[0]:
				return stringContain(s1, s2[1:], s3[1:])
		return False
	if len(s1) == len(s2) == 0:
		return True
	return False

	
print("Desired Output (T/F) : Actual Output (True/False)")
print("T : " + str(stringContain("abcde", "vwxyz", "vwxabcdeyz")))
print("F : " + str(stringContain("abcde", "vwxyz", "vwxabcde")))
print("T : " + str(stringContain("abcde", "vwxyz", "vwxyzabcde")))
print("T : " + str(stringContain("abcde", "vwxyz", "abcvwxdeyz")))
print("T : " + str(stringContain("abcde", "vwxyz", "abcdevwxyz")))
print("T : " + str(stringContain("abcde", "vwxyz", "avwxyzbcde")))
print("F : " + str(stringContain("acac", "aadd", "acadadc")))
print("T : " + str(stringContain("acac", "aadd", "aacaddac")))
print("T : " + str(stringContain("ab", "bx", "abxb")))
print("T : " + str(stringContain("ab", "aaaaad", "aaaaadab")))
print("F : " + str(stringContain("ab", "aaaaad", "abaaaada")))
print("F : " + str(stringContain("ab", "aaaaad", "aaaaadba")))
print("F : " + str(stringContain("ab", "bc", "abbcxxx")))
print("F : " + str(stringContain("ab", "bc", "xxxabbc")))

