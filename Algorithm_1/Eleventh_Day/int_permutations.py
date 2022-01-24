from typing import List
SOL = []
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        global SOL
        SOL.clear()
        permutations(nums, [])
        return SOL
        
        
        
def permutations(nums, sel):
    if len(nums) == 0:
        global SOL
        SOL.append(sel)
        return 
    for i in range(len(nums)):
        permutations(nums[:i]+nums[i+1:], sel + [nums[i]])

def test(nums, ans):
	s = Solution()
	r = s.permute(nums)

	assert r == ans


if __name__ == "__main__":
	nums = [1,2,3]
	ans = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
	test(nums, ans)

	nums = [0,1]
	ans =  [[0,1],[1,0]]
	test(nums, ans)

	nums = [1]
	ans = [[1]]
	test(nums, ans)	
