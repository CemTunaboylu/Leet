from typing import List 

LIM_X = None
LIM_Y = None
class Solution:
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		# All I need is to remember the biggest
		field = 0
		global LIM_X, LIM_Y, visited
		LIM_X = len(grid[0])-1
		LIM_Y = len(grid)-1
		for y in  range(LIM_Y+1):
			for x in range(LIM_X+1):
				if grid[y][x] == 1:
					a = bfs(grid, (y,x) )
					field = max(field, a )
		
		return field

def bfs(grid, coor):
	q = [coor]
	size = 0
	while len(q) > 0:
		print(f"q : {q}")
		coor = q.pop(0)
		if grid[coor[0]][coor[1]] == 0:
			continue
		grid[coor[0]][coor[1]] = 0
		size += 1
		ns = neighbors(coor)
		for n in ns:
			if grid[ n[0] ][ n[1] ] == 1:
				q.append(n)
		print(f"ns : {ns}")
		print(f"size : {size}")

	return size
		



def neighbors(tup):
	n = []
	if tup[0] > 0:
		n.append( (tup[0]-1, tup[1]) )
	if tup[0] < LIM_Y:	
		n.append( (tup[0]+1, tup[1]) )
	if tup[1] > 0:
		n.append( (tup[0], tup[1]-1) )
	if tup[1] < LIM_X:
		n.append( (tup[0], tup[1]+1) )

	return n 

def test(grid, ans):
	s = Solution()
	r = s.maxAreaOfIsland(grid)
	#print(f"result {r}")
	assert ans == r 	
if __name__ == "__main__":
	grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
	#test(grid, 6)
	grid = [[0,0,0,0,0,0,0,0]]
	#test(grid, 0)

	#grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
	grid = [[1,1]]
	test(grid, 2)

	
