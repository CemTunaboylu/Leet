# rotate the list to the right by k
def rotate(nums, k):
	k %= len(nums)
	if len(nums) == 1 or k == 0:
		return
	reverse(nums, 0, len(nums)-1)	
	reverse(nums, 0, k-1)
	reverse(nums, k, len(nums)-1)

def reverse(l, s, e):
	while s < e:
		t = l[s]
		l[s] = l[e]
		l[e] = t
		s += 1
		e -= 1

def test(nums, k):
	rotate(nums, k)
	print(nums)

if __name__ == "__main__":
	nums, k = [1,2,3,4,5,6,7],  3 
	test(nums,k)

	nums = [1,2,3,4,5,6]
	k = 2
	test(nums,k)

	nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
	k = 45
	test(nums,k)

	nums, k = [1,2], 3
	test(nums, k)
