from typing import List
def sortedSquares(nums: List[int]) -> List[int]:

        if len(nums) == 1:
                return [nums[0] ** 2]

        l = len(nums)
                
        if nums[0] >= 0:
                return only_positives(nums, l)
        elif nums[-1] <= 0:
                return only_negatives(nums, l)

        mem = find_zero(nums,l)
        print(f"mem : {mem}")

        negatives = only_negatives(nums[:mem], mem)
        positives = only_positives(nums[mem:], l - mem)

        i = 0
        while len(positives) > 0 and len(negatives) > 0:
                if len(positives) == 0:
                        for n in negatives:
                                nums[i] = n
                                i += 1
                        return nums
                if len(negatives) == 0:
                        for p in positives:
                                nums[i] = p
                                i += 1
                        return nums
                if negatives[0] > positives[0]:
                        nums[i] = positives.pop(0)
                else:
                        nums[i] = negatives.pop(0)
                i += 1

        return nums

def only_positives(nums, l):
        for i in range(l): # ->  time : O(n) 
                nums[i] = nums[i] ** 2 
        print(f"+ nums: {nums} ")
        return nums

def only_negatives(nums, l):
        for i in range(l): # ->  time : O(n) 
                nums[-i] = nums[-i] ** 2 
        nums.reverse()
        print(f"- nums: {nums} ")
        return nums
    
def find_zero(nums, l):
        high = l
        low = 0 
        mem = high

        while high > low: # ->  time : O(n) 
                m = (high+low)//2
                if nums[m] == 0:
                        return m 
                if nums[m] > 0:
                        high = m 
                        mem = low
                elif nums[m] < 0:
                        low = m + 1
                        mem = high

        return mem


# [-7,-3,2,3,11]
nums = [-1,2,2]
print(f"Working on {nums}")
print(sortedSquares(nums))
