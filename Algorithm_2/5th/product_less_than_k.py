from functools import reduce
from typing import List
class Solution:
	def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
		if len(nums) == 0 or k==0:
			return 0 
		count = 0 # 1 if nums[0] < k else 0
		i,j = 0,0    
		p = 1
		while j < len(nums):
			p *= nums[j] 
			while p>=k and i<=j:
				p /= nums[i]
				i+=1
			count += (j-i+1)
			j+=1
		
		return count
def test(nums, k, a):
	s = Solution()
	r = s.numSubarrayProductLessThanK(nums, k)
	print(F"r:{r}, a:{a}")
	assert r==a

if __name__ == "__main__":
	nums = [10,5,2,6]
	k = 100
	test(nums,k, 8)
	nums = [1]*9044
	k = 373466
	test(nums,k,40901490)
	nums = [1]*3
	k = 1
	test(nums,k,0)
	 
        
