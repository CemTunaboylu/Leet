from typing import List
SOL = set()
class Solution:
	def letterCasePermutation(self, s: str) -> List[str]:
		if len(s) == 1:
			if s[0].isalpha():
				return [ s.lower(), s.upper() ]
			else:
				return [s]
		s_l = list(s)
		perm(s_l, 0)
		return list(SOL)
    
    
def perm(my_str, start):
	for i in range(start, len(my_str)):
		if not my_str[i].isalpha():
			continue
		perm( my_str[:i]+[my_str[i].upper()]+my_str[i+1:], start+1)
		perm( my_str[:i]+[my_str[i].lower()]+my_str[i+1:], start+1)
	a = "".join(my_str)
	global SOL
	if not a in SOL:
		SOL.add(a)

def test(s, a):
	sol = Solution()
	r = sol.letterCasePermutation(s)
	r_s = set(r)
	r_a = set(a)

	diff = r_a.difference(r_s)
	if not len(diff) == 0:
		print(list(diff))
if __name__ == "__main__":
	s = "a"
	a = ["a", "A"]
	test(s,a)
	
	s = "0"
	a = ["0"]
	test(s,a)
	s = "a1b2"
	a = ["a1b2","a1B2","A1b2","A1B2"]
	test(s,a)

	s = "abc"
	a = ["abc","abC","aBc","aBC","Abc","AbC","ABc","ABC"]
	test(s,a)	
	
	#s = "k5qo0LdW"
	#test(s, a)
