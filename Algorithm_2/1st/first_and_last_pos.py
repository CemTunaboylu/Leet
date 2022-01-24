from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target < nums[0] or target > nums[-1]:
            return [-1,-1]

        anchor = binary_search(nums, target, 0, len(nums)-1)
        # smaller larger constraints
        if anchor == -1:
            return [-1, -1]
        
        low = binary_search(nums, target, 0, (len(nums)-1)//2)
        high = binary_search(nums, target, (len(nums)-1)//2, len(nums)-1)

        print(f"high : {high}, low : {low}")
        # low_test=low
        # high_test = high
        # arr = nums[:]
        
        # while low_test!=-1:
        #     print(f"Low : {low}, low_test : {low_test}")
        #     arr = arr[:low_test]
        #     low_test = binary_search(arr, target)
        #     if low_test<low and low_test!=-1:
        #         low = low_test

        # arr = nums[:]
        # while high_test !=-1 :
        #     print(f"High : {high}, high_test : {high_test}")
        #     arr = arr[high_test+1:]
        #     high_test = binary_search(arr, target)
        #     if high_test + anchor > high and high_test!=-1:
        #         high = high_test + anchor
            
        # print(F"nums : {nums}")
        # if high < 0:
        #     high = anchor
        # if low < 0:
        #     low = anchor
        # print(f"high : {high}, low : {low}")
        # return [low, high]
        
        
def binary_search(nums, target, low, high):    
    while low<=high:
        mid = (low+high)//2
    
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid+1
        else:
            high = mid-1
            
    return -1

def test(t, a=[5,7,7,8,8,10]):
    s = Solution()
    r = s.searchRange(a,t)
    print(f"Position range of {t} is {r}")

def tests():
    test(1)
    # test(5)
    # test(7)
    # test(8)
    # test(9)
    # test(10)
    # test(11)
    # test(1, [1])
    # test(1, [0])
    # test(1, [2])
    # test(1, [1,1,1,1,1])


a = [1,2,2,2,2,6,7,8] #,3,4,5
print(a)
s = Solution()
s.searchRange(a, 2)

# tests()
