from functools import reduce
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0 
        nums.sort() # Timsort
        if nums[0] > k:
            return 0
        count = 0
        drop = False
        window_size = 1
        while not drop:
            for i in range(len(nums)-window_size):
                p = reduce( (lambda x,y: x*y) ,nums[i: i+window_size] )
                print(f"window:{window_size}, nums:{nums[i: i+window_size]} w/ product:{p} ")
                if p<k:
                    count += 1
                else:
                    break
            if i==0:
                drop = True
                
            window_size += 1
        
        return count

nums = [10,5,2,6]
k = 100
s = Solution()
r = s.numSubarrayProductLessThanK(nums, k)
print(r)
                
        
        