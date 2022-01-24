# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers 
# such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

#Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#The tests are generated such that there is exactly one solution. You may not use the same element twice.


def two_sum(arr, target):
	l = len(arr)
	if l < 2:
		raise ValueError("array do not have sufficient elements, at least 2 required.")
	left = 0
	right = l-1
	
	while left < right:
		sum = arr[left] + arr[right]
		if sum == target:
			return [ left+1, right+1 ]
		if sum < target:
			left += 1
		if sum > target:
			right -= 1

	return [None, None]


def test(arr, t, ans):
	sol = two_sum(arr, t)
	assert sol == ans


arr = [2,7,11,15] 
t = 9

test(arr, t, [1,2])
