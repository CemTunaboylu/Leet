def rot(a, k):
	a[:k],a[k:] = a[-k:], a[:-k]

def test(nums, k):
	rot(nums, k)
	print(nums)
def debug():

		a, k = [1,2,3,4,5,6,7,8,9], 3
		print(f"a : {a}")
		print(f"a[-k:] : {a[-k:]} ")
		print(f"a[:k] : {a[:k]} ")
		print(f"a[k:] : {a[k:]} ")
		print(f"a[:-k] : {a[:-k]} ")

		rot(a, k)
		print(f"a : {a}")

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

