# Given an array, rotate the array to the right by k steps, where k is non-negative.

from typing import List 
class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		l = len(nums)
		if k == l or k == 0:
			return 
		if k*2 == l:
			for i in range(k):
				swap(nums,i, i+k)
			return
		shift = l%k == 0    
		counter = 0
		i = 0
		temp = nums[i]
		start = 0
		while counter < l:
			n = (i+k)%l
			prev = nums[n]
			nums[n] = temp
			temp = prev
			i = n
			if i == start:
				# change is already happened
				i += 1
				temp = nums[i]
				start = i
			counter += 1
            
def swap(arr, i, j):
	arr[i] = arr[i]^arr[j]
	arr[j] = arr[i]^arr[j]
	arr[i] = arr[i]^arr[j]
   
def test(nums, k):
	s = Solution()
	s.rotate(nums, k)

	print(nums)
if __name__ == "__main__":
	#nums, k = [1,2,3,4,5,6,7],  3 
	#test(nums,k)

	#nums = [1,2,3,4,5,6]
	#k = 2
	#test(nums,k)

	nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
	k = 45
	test(nums,k)
