"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.
Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""

from typing import List
SOL = None
class Solution:
	def letterCasePermutation(self, s: str) -> List[str]:
		if len(s) == 1:
			if s[0].isalpha():
				return [ s.lower(), s.upper() ]
			else:
				return [s]
		global SOL
		SOL = []

		perm(s, 0)
		return SOL
    
    
def perm(my_str, mutation_index):
	if mutation_index == len(my_str):
		global SOL
		SOL.append( my_str )
		return
	if not my_str[mutation_index].isalpha():
		perm( my_str, mutation_index+1)
	else:
		perm( my_str[:mutation_index]+my_str[mutation_index].upper()+my_str[mutation_index+1:], mutation_index+1)
		perm( my_str[:mutation_index]+my_str[mutation_index].lower()+my_str[mutation_index+1:], mutation_index+1)
	

def test(s, a):
	sol = Solution()
	r = sol.letterCasePermutation(s)
	r_s = set(r)
	r_a = set(a)

	diff = r_a.difference(r_s)
	if not len(diff) == 0:
		print(list(diff))
if __name__ == "__main__":
	s,a = "a",["a", "A"]
	test(s,a)
	
	s,a = "0", ["0"]
	test(s,a)
	s,a = "a1b2", ["a1b2","a1B2","A1b2","A1B2"]
	test(s,a)

	s,a = "abc", ["abc","abC","aBc","aBC","Abc","AbC","ABc","ABC"]
	test(s,a)	
	
	s,a = "k5qo0LdW",["k5qo0ldw","k5qo0ldW","k5qo0lDw","k5qo0lDW","k5qo0Ldw","k5qo0LdW","k5qo0LDw","k5qo0LDW","k5qO0ldw","k5qO0ldW","k5qO0lDw","k5qO0lDW","k5qO0Ldw","k5qO0LdW","k5qO0LDw","k5qO0LDW","k5Qo0ldw","k5Qo0ldW","k5Qo0lDw","k5Qo0lDW","k5Qo0Ldw","k5Qo0LdW","k5Qo0LDw","k5Qo0LDW","k5QO0ldw","k5QO0ldW","k5QO0lDw","k5QO0lDW","k5QO0Ldw","k5QO0LdW","k5QO0LDw","k5QO0LDW","K5qo0ldw","K5qo0ldW","K5qo0lDw","K5qo0lDW","K5qo0Ldw","K5qo0LdW","K5qo0LDw","K5qo0LDW","K5qO0ldw","K5qO0ldW","K5qO0lDw","K5qO0lDW","K5qO0Ldw","K5qO0LdW","K5qO0LDw","K5qO0LDW","K5Qo0ldw","K5Qo0ldW","K5Qo0lDw","K5Qo0lDW","K5Qo0Ldw","K5Qo0LdW","K5Qo0LDw","K5Qo0LDW","K5QO0ldw","K5QO0ldW","K5QO0lDw","K5QO0lDW","K5QO0Ldw","K5QO0LdW","K5QO0LDw","K5QO0LDW"]
	test(s, a)

	s = "LzYracpd"
	a = ['LZYRACPD', 'LZYRACPd', 'LZYRACpD', 'LZYRACpd', 'LZYRAcPD', 'LZYRAcPd', 'LZYRAcpD', 'LZYRAcpd', 'LZYRaCPD', 'LZYRaCPd', 'LZYRaCpD', 'LZYRaCpd', 'LZYRacPD', 'LZYRacPd', 'LZYRacpD', 'LZYRacpd', 'LZYrACPD', 'LZYrACPd', 'LZYrACpD', 'LZYrACpd', 'LZYrAcPD', 'LZYrAcPd', 'LZYrAcpD', 'LZYrAcpd', 'LZYraCPD', 'LZYraCPd', 'LZYraCpD', 'LZYraCpd', 'LZYracPD', 'LZYracPd', 'LZYracpD', 'LZYracpd', 'LZyRACPD', 'LZyRACPd', 'LZyRACpD', 'LZyRACpd', 'LZyRAcPD', 'LZyRAcPd', 'LZyRAcpD', 'LZyRAcpd', 'LZyRaCPD', 'LZyRaCPd', 'LZyRaCpD', 'LZyRaCpd', 'LZyRacPD', 'LZyRacPd', 'LZyRacpD', 'LZyRacpd', 'LZyrACPD', 'LZyrACPd', 'LZyrACpD', 'LZyrACpd', 'LZyrAcPD', 'LZyrAcPd', 'LZyrAcpD', 'LZyrAcpd', 'LZyraCPD', 'LZyraCPd', 'LZyraCpD', 'LZyraCpd', 'LZyracPD', 'LZyracPd', 'LZyracpD', 'LZyracpd', 'LzYRACPD', 'LzYRACPd', 'LzYRACpD', 'LzYRACpd', 'LzYRAcPD', 'LzYRAcPd', 'LzYRAcpD', 'LzYRAcpd', 'LzYRaCPD', 'LzYRaCPd', 'LzYRaCpD', 'LzYRaCpd', 'LzYRacPD', 'LzYRacPd', 'LzYRacpD', 'LzYRacpd', 'LzYrACPD', 'LzYrACPd', 'LzYrACpD', 'LzYrACpd', 'LzYrAcPD', 'LzYrAcPd', 'LzYrAcpD', 'LzYrAcpd', 'LzYraCPD', 'LzYraCPd', 'LzYraCpD', 'LzYraCpd', 'LzYracPD', 'LzYracPd', 'LzYracpD', 'LzYracpd', 'LzyRACPD', 'LzyRACPd', 'LzyRACpD', 'LzyRACpd', 'LzyRAcPD', 'LzyRAcPd', 'LzyRAcpD', 'LzyRAcpd', 'LzyRaCPD', 'LzyRaCPd', 'LzyRaCpD', 'LzyRaCpd', 'LzyRacPD', 'LzyRacPd', 'LzyRacpD', 'LzyRacpd', 'LzyrACPD', 'LzyrACPd', 'LzyrACpD', 'LzyrACpd', 'LzyrAcPD', 'LzyrAcPd', 'LzyrAcpD', 'LzyrAcpd', 'LzyraCPD', 'LzyraCPd', 'LzyraCpD', 'LzyraCpd', 'LzyracPD', 'LzyracPd', 'LzyracpD', 'Lzyracpd', 'lZYRACPD', 'lZYRACPd', 'lZYRACpD', 'lZYRACpd', 'lZYRAcPD', 'lZYRAcPd', 'lZYRAcpD', 'lZYRAcpd', 'lZYRaCPD', 'lZYRaCPd', 'lZYRaCpD', 'lZYRaCpd', 'lZYRacPD', 'lZYRacPd', 'lZYRacpD', 'lZYRacpd', 'lZYrACPD', 'lZYrACPd', 'lZYrACpD', 'lZYrACpd', 'lZYrAcPD', 'lZYrAcPd', 'lZYrAcpD', 'lZYrAcpd', 'lZYraCPD', 'lZYraCPd', 'lZYraCpD', 'lZYraCpd', 'lZYracPD', 'lZYracPd', 'lZYracpD', 'lZYracpd', 'lZyRACPD', 'lZyRACPd', 'lZyRACpD', 'lZyRACpd', 'lZyRAcPD', 'lZyRAcPd', 'lZyRAcpD', 'lZyRAcpd', 'lZyRaCPD', 'lZyRaCPd', 'lZyRaCpD', 'lZyRaCpd', 'lZyRacPD', 'lZyRacPd', 'lZyRacpD', 'lZyRacpd', 'lZyrACPD', 'lZyrACPd', 'lZyrACpD', 'lZyrACpd', 'lZyrAcPD', 'lZyrAcPd', 'lZyrAcpD', 'lZyrAcpd', 'lZyraCPD', 'lZyraCPd', 'lZyraCpD', 'lZyraCpd', 'lZyracPD', 'lZyracPd', 'lZyracpD', 'lZyracpd', 'lzYRACPD', 'lzYRACPd', 'lzYRACpD', 'lzYRACpd', 'lzYRAcPD', 'lzYRAcPd', 'lzYRAcpD', 'lzYRAcpd', 'lzYRaCPD', 'lzYRaCPd', 'lzYRaCpD', 'lzYRaCpd', 'lzYRacPD', 'lzYRacPd', 'lzYRacpD', 'lzYRacpd', 'lzYrACPD', 'lzYrACPd', 'lzYrACpD', 'lzYrACpd', 'lzYrAcPD', 'lzYrAcPd', 'lzYrAcpD', 'lzYrAcpd', 'lzYraCPD', 'lzYraCPd', 'lzYraCpD', 'lzYraCpd', 'lzYracPD', 'lzYracPd', 'lzYracpD', 'lzYracpd', 'lzyRACPD', 'lzyRACPd', 'lzyRACpD', 'lzyRACpd', 'lzyRAcPD', 'lzyRAcPd', 'lzyRAcpD', 'lzyRAcpd', 'lzyRaCPD', 'lzyRaCPd', 'lzyRaCpD', 'lzyRaCpd', 'lzyRacPD', 'lzyRacPd', 'lzyRacpD', 'lzyRacpd', 'lzyrACPD', 'lzyrACPd', 'lzyrACpD', 'lzyrACpd', 'lzyrAcPD', 'lzyrAcPd', 'lzyrAcpD', 'lzyrAcpd', 'lzyraCPD', 'lzyraCPd', 'lzyraCpD', 'lzyraCpd', 'lzyracPD', 'lzyracPd', 'lzyracpD', 'lzyracpd']
	test(s, a)
