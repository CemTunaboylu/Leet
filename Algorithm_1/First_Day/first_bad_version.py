"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

constraints: 
1 <= bad <= n <= 2^31 - 1

""" 

BAD_VERSION = None
def isBadVersion(n):
	return n>=BAD_VERSION	

def bfs_first_bad(arr_size):
	if isBadVersion(1):
		return 1 
	low = 1

	while n >= low:
		mid  = (n+low)//2
		if isBadVersion(mid):
			n = mid-1
		else:
			low = mid+1
	return low

def test(arr_size, f_b):
	global BAD_VERSION
	BAD_VERSION = f_b
	
	r = bfs_first_bad(arr_size)
	print(f" r: {r}, f_b {f_b}")
	assert r == f_b

if __name__ == "__main__":
	test(5, 4)
	test(1,1)

