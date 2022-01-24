class Result:
	def __init__(self, _m, _e=False):
		self.mem = _m
		self.exists = _e

def search_matrix(matrix, target):
	r = col_search(matrix, target)
	if r.exists:
		return True
	return binary_search(matrix[r.mem], target)
	

def col_search(matrix, target):
	low=0
	high = len(matrix)-1
	mem=high
	r = Result(mem)
	while low<=high:
		mid = (low+high)//2 # integer div
		if matrix[mid][0] == target:
			r.exists = True
			return r
		elif matrix[mid][0] < target:
			low=mid+1
			mem=mid
		else: # matrix[mid][0] > target:
			high = mid -1
			mem= high

	r.mem = mem
	return r

def binary_search(matrix, target):
	low = 0
	high = len(matrix)-1

	while low<=high:
		mid = (low+high)//2
		if matrix[mid] == target:
			return True
		elif matrix[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	
	return False



def test(matrix, target, a):
	assert a == search_matrix(matrix, target)

if __name__ == "__main__":
	m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
	for row in m:
		for t in row:
			test(m,t,True)
	
	t= [-1, 6, 9, 15, 19, 21, 24, 29, 59, 64]
	for e in t:
		test(m,e,False)
	
	m = [ [[23,30,34,60]] ]
	for row in m:
		for t in row:
			test(m,t,True)
	t= [-1, 6, 9, 15, 19, 21, 24, 29, 59, 64]
	for e in t:
		test(m,e,False)
