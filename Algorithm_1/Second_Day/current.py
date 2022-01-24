from typing import List
class Solution:
        def sortedSquares(self, nums: List[int]) -> List[int]:

                if len(nums) == 1:
                        return [nums[0] ** 2]

                l = len(nums)
                if nums[0] >= 0:
                        return only_positives(nums, l)
                elif nums[-1] <= 0:
                        r = only_negatives(nums, l)
                        r.reverse()
                        return r

                mem = find_zero(nums,l)

                negatives = only_negatives(nums[:mem], mem)
                positives = only_positives(nums[mem:], l - mem)

                i = 0
                while len(positives) > 0 or len(negatives) > 0:
                        if len(positives) == 0:
                                # i = len(nums) - 1
                                negatives.reverse()
                                nums[-len(negatives):] = negatives[:]
                                # for n in negatives:
                                #         nums[i] = n
                                #         i -= 1
                                return nums
                        if len(negatives) == 0:
                                nums[-len(positives):] = positives[:]
                                # for p in positives:
                                #         nums[i] = p
                                #         i += 1
                                return nums
                        if negatives[-1] > positives[0]:
                                nums[i] = positives.pop(0)
                        else:
                                nums[i] = negatives.pop(-1)
                        i += 1

                return nums

def only_positives(nums, l):
        for i in range(l): # ->  time : O(n) 
                nums[i] = nums[i] ** 2 
        return nums

def only_negatives(nums, l):
        for i in range(l): # ->  time : O(n) 
                nums[-i] = nums[-i] ** 2 
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
def test():
        r = [36,16,9,4,2,1]
        l = [1,2,3,4,5,6,7,8,9,10,0,0,0,0,0,0]

        r.reverse()
        l[-len(r):] = r[:]
        print(f"l: {l}")




test()