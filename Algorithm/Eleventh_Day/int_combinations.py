from typing import List
N = None
SOL = []

class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		global N
		SOL.clear() # for multiple runs on the same execution, SOL will be already populated
		N = k
		combinations(list(range(1,n+1)), []) 
		return SOL

def combinations(opts, sel):
	if len(sel) == N:
		global SOL
		SOL.append(sel[:])
		return
	for i in range(len(opts)):
		# combinations(opts[:i]+opts[i+1:], sel + [opts[i]] ) #permutations
		combinations(opts[i+1:], sel + [opts[i]] )

def test(n=4,k=2):
	from itertools import combinations
	s = Solution()
	r = s.combine(n,k)
	c = list(combinations(range(1,n+1), k))
	print(r)
	print(c)
	for com in c:
		com = list(com)
		r.remove(com)

	assert len(r) == 0

test()
# test(2,1)