from typing import List

def sortedSquares(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
                return [nums[0] ** 2]
        
        l = len(nums)
            
        if nums[0] >= 0:
                return only_positives(nums, l)
        elif nums[-1] <= 0:
                return only_negatives(nums, l)
        
        m = max( abs(nums[0]), nums[-1] ) + 1 
        sqrs = [0]*m

        for i in range(l): # ->  time : O(n) 
                elm = abs( nums[i] )
                sqrs[elm] += 1  

        where_in_nums = 0
        for i in range(m):# -> time : O(n)
                amt = sqrs[i]
                if amt > 0:
                        sq = i**2
                        while amt > 0:
                                nums[where_in_nums] = sq
                                where_in_nums += 1
                                amt -= 1

        return nums

def only_positives(nums, l):
        for i in range(l): # ->  time : O(n) 
                nums[i] = nums[i] ** 2 
        return nums

def only_negatives(nums, l):
        for i in range(l): # ->  time : O(n) 
                nums[-i] = nums[-i] ** 2 
        nums.reverse()
        return nums