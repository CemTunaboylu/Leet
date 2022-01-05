from typing import List
from big_list import b_l
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
class Solution:
    def moveZeroes(self, n: List[int]) -> None:
        if len(n) < 1:
            return
        n_c = 0
        i = 0
        while i < len(n):
            if n[i] == 0:
                n_c += 1
                del n[i]
                i -= 1
            i += 1
        n.extend([0]*n_c)
def test(n, c=None):
	s = Solution()
	#print(n)
	if not c:
		c = correct(n)
	s.moveZeroes(n)
	assert c == n

def correct(n):
	n_c = n.count(0)
	n = list(filter(lambda a: a !=0, n))
	n += [0]*n_c
	return n

#n = [0,1,0,3,12]
n = b_l
#a = [1,3,12,0,0]
test(n)


