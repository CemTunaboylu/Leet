# Definition for a binary tree node.
from bst_methods import BSTNode, insert
from bst_methods import pre_order as order
from typing import List, Optional 

class Solution:
    def mergeTrees(self, root1: Optional[BSTNode], root2: Optional[BSTNode]) -> Optional[BSTNode]:
        if not root1 and root2:
            return root2
        if not root2 and root1:
            return root1
        if not root1 and not root2:
            return None
        merge(root1,root2)
        return root1
        
        
        
def merge(r1, r2):
    if r1 and r2:
        r1.data += r2.data
    
    if not r1.left and r2.left:
        r1.left = BSTNode(0)
    if r1.left and r2.left:
        merge(r1.left, r2.left)
        
    if not r1.right and r2.right:
        r1.right = BSTNode(0)
    if r1.right and r2.right:
        merge(r1.right, r2.right)

def test(l1, l2):
	r1, r2 = None, None
	for e1 in l1:
		r1 = insert(r1, e1, node_type="bst_methods.BSTNode")
	for e2 in l2:
		r2 = insert(r2, e2, node_type="bst_methods.BSTNode")
	
	order(r1)
	print()
	order(r2)
	print()	
	
	s = Solution()
	r1 = s.mergeTrees(r1,r2)	
	order(r1)
	print()
if __name__ == "__main__":
		l1 = [3,2,1,5]
		l2 = [3,2,1,4,7]	
		test(l1,l2)	

