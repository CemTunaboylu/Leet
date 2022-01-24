from typing import List

LIM_X = None
LIM_Y = None

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        queue = [(sr, sc)] # (y,x)
        old_color = image[sr][sc]
        
        global LIM_X, LIM_Y
        LIM_X = len(image[0])-1
        LIM_Y = len(image)-1
        
        while len(queue) > 0:
            cur_coor = queue.pop(0)    
            image[cur_coor[0]][cur_coor[1]] = newColor
            ns = neighbors(cur_coor)
            for n in ns:
                if image[n[0]][n[1]] == old_color:
                    queue.append(n)
        
        return image
                
        
def neighbors(tup):

    n = []
    if tup[0] > 0:
        n.append( (tup[0] - 1, tup[1] ) )
    if tup[0] < LIM_Y:
        n.append( (tup[0] + 1, tup[1] ) )
    if tup[1] > 0:
        n.append( (tup[0], tup[1]- 1 ) )
    if tup[1] < LIM_X:
        n.append( (tup[0], tup[1]+ 1 ) )
        
    return n


def test():
	img = [[1,1,1],[1,1,0],[1,0,1]]
	sr = 1
	sc = 1
	s = Solution()
	newColor = 2
	r = s.floodFill(img, sr, sc, newColor)
	a = [[2,2,2],[2,2,0],[2,0,1]]
	assert a == r 
test()
