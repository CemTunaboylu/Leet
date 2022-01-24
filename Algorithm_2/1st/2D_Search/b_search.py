def search_matrix(matrix, target):
        low_x = 0
        low_y = 0
        high_x = len(matrix[0])-1
        high_y = len(matrix)-1
        while low_x<=high_x and low_y<=high_y:
                mid_x, mid_y = (low_x+high_x)//2,  (low_y+high_y)//2  
                if matrix[mid_y][mid_x] == target:
                        return True
                if matrix[mid_y][-1] < target:
                        low_y=mid_y+1
                elif matrix[mid_y][mid_x] < target: # in this row
                        low_x=mid_x+1
                if matrix[mid_y][0] > target: # matrix[mid][0] > target:
                        high_y=mid_y-1
                elif matrix[mid_y][mid_x] > target:
                        high_x = mid_x-1
        
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
	
	m = [ [23,30,34,60] ]
	for row in m:
		for t in row:
			test(m,t,True)
	t= [-1, 6, 9, 15, 19, 21, 24, 29, 59, 64]
	for e in t:
		test(m,e,False)
