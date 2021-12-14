"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

* 1 <= nums.length <= 10^4
* -104 <= nums[i] <= 10^4
* nums contains distinct values sorted in ascending order.
* -10^4 <= target <= 10^4

"""

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
	l = len(nums)
	if l < 2:
		if nums[0] == target:
			return 0
		return 0 if nums[0] > target else 1

	if nums[0] > target:
		return 0
	elif nums[-1] < target:
		return l	

	high = l
	low = 0
	mem = 0
	while high>low:
		mid = (high+low)//2
		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			high = mid
			mem = low
		else:
			low = mid+1
			mem = high
	return mem 


def test(nums, target, ans):
	print(f"Testing on {nums} target:{target} ")
	r = searchInsert(nums, target)
	print(f"r : {r}, ans : {ans}")
	assert r == ans

if __name__ == "__main__":
	test( [1,3,5,6], 5, 2)
	test( [1,3,5,6], 7, 4)
	test( [1,3,5,6], 0, 0)
	test( [1], 0, 0)
	test( [1], 2, 1)
	test( [1,3,5,6], 2, 1)
	test([1,3], 2, 1)
	
