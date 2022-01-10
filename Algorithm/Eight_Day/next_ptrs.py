
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.data = val
        self.left = left
        self.right = right
        self.next = next

from next_ptrs_iter import conn as connect
from bst_methods import BSTNode, insert
from bst_methods import pre_order as order
class Solution:
	def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
		#conn(root)
		connect(root)
		return root
        

def conn(root):
    if not root or not root.left: # since perfect, left None means right None
        return  
    if root.left: # has children 
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
    if root.left.left: # has grandchildren
        conn(root.left)
        conn(root.right)
        
def print_lv(root):
	t = root
	while t:
		r = t
		while r:
			print(f"{r.data}", end=" ")
			if not r.next:
				break
			r = r.next
		if not t.left:
			break
		t = t.left
		print("#", end=" ")
	#while t.next:
	#	print(f"{t.data}", end=" ")
	#	t = t.next
	#print("#", end="")

def test(l):
	r = None
	for e in l:
		r = insert(r, e, node_type=__name__+".Node")
	order(r)
	print()
	s = Solution()
	r = s.connect(r)

	print_lv(r)

test( [4,2,3,1,6,5,7] )

