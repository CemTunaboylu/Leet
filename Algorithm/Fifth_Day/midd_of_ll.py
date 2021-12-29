# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #runners method
        if not head or not head.next:
            return head
         
        t = head
        r = head

        while r.next and r.next.next:
            t = t.next
            r = r.next.next

        if r.next:
            t = t.next

        return t

def test():
    s = Solution()
    head = ListNode(1)
    t = head
    for i in range(2,6):
        t.next = ListNode(i)
        t = t.next

    # t = head
    # while t.next != None:
    #     print(f"->{t.val}", end="")
    #     t = t.next
    # print(f"->{t.val}", end="")

    # print()
    p = s.middleNode(head)
    assert p.val == 3
    # print(p.val)

        
test()