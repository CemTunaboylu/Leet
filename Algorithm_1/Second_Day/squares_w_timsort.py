from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
	if len(nums) == 1:
		return [nums[0] ** 2]
	l = len(nums)
	reverse = False
	if nums[-1] <= 0:
		reverse = True

	for i in range(l): # ->  time : O(n) 
		nums[i]  = nums[i]**2
	if reverse:
		nums.reverse()
	else:
		#Timsort
		nums.sort()

	return nums 


def test():
	nums = [-4,-1,0,3,10]
	out = sortedSquares(nums)
	ans = [0,1,9,16,100]
	assert out == ans


if __name__ == "__main__":
	test()
