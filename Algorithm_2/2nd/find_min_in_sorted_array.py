""" 

a = [4,5,6,7,0,1,2]

if k%len(a) < len(a) - 1 where k is the rotation time of the array, the following will happen eventually:

a[p] > a[p+1]  : this is the breaking point. a[p+1] is the smallest element

Normally in binary search, 

	mid = (high+low)//2 
	if a[mid] < target:
		low = mid+1
	elif a[mid] > target:
		high = mid 

"""




def binary_search(nums):
	if len(nums) < 3:
		return min(nums[0], nums[1]) if len(nums) == 2 else nums[0]
	low, high = 0, len(nums)-1

	mid = (low+high)//2
	print(f" mid:{mid} value : {nums[mid]} ")
	if nums[mid-1] > nums[mid+1]:
		return min(nums[mid], nums[mid+1])
	else:
		p1 = binary_search(nums[:mid])
		p2 = binary_search(nums[mid+1:])

	return min(p1,p2)

#a = [4,5,6,7,0,1,2,3]
a = [6,7,0,1,2,3,4,5]
print(a)
r = binary_search(a)

print(r)




