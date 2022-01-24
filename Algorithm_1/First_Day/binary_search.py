
def search(nums, target):
        
	if nums[0] > target or nums[-1] < target:
		return -1
        
	low = 0 
	high = len(nums)-1

	while high >= low :
		mid = (low+high)//2 # this can overflow if array is too big, but not concerned with this
		if nums[mid] == target:
			return mid

		elif nums[mid] > target:
			high = mid-1
		else: 
			low = mid+1 
	return -1 	


def test(nums = [-1,0,3,5,9,12], target = 9):

	i =  search(nums, target)
	#print(f"Result : {i}")
	return i

if __name__ == "__main__":
	assert test() == 4
	assert test(target=2) == -1
	assert test(nums=[5], target=5) == 0
	assert test(nums=[2,5], target=5) == 1
	assert test(nums=[-1,0,3,5,9,12], target=13) == -1
	assert test(nums=[-1,0,3,5,9,12], target=-13) == -1
