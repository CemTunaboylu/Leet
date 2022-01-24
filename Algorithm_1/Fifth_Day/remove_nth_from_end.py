# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
                raise ValueError(f"n should be a positive integer.")
        if not head:
                return head
        if not head.next and n == 1:
                del head 
                return None
        #runners method
        t = head
        r = head
        l = 1
        m = 1
        while r.next and r.next.next:
                t = t.next
                r = r.next.next
                l += 2
                m += 1

        if r.next:
                l += 1
        if n > l:
                raise ValueError(f"Value of n({n}) is longer than the list ({l}).")

        if r.next and n == 1:
                r.next = None
                return head
        elif n == l: # it is the head that we need to remove
                rem = head
                head = head.next
                return head
        i = l - n

        if m <= i: # it is later than mid
                while m < i:
                        t = t.next
                        m += 1
                t.next = t.next.next
        else: # it is before the mid +++
                # 1->2->3->4->5->6 # n = 5 (2), i = 1
                c = head
                while i > 1:
                        c = c.next
                        i -= 1
                rem = c.next
                c.next = c.next.next                
        return head

def print_ll(head):
    t = head
    while t.next != None:
        print(f"->{t.val}", end="")
        t = t.next
    print(f"->{t.val}", end="")
    print()

def test(rem_index, head=None):
    s = Solution()
    if not head:
        head = ListNode(1)
        t = head
        for i in range(2,6):
                t.next = ListNode(i)
                t = t.next

    print_ll(head)
    try:
        head = s.removeNthFromEnd(head, rem_index)
        print_ll(head)
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    test(0)
    test(1)
    test(2)
    test(3)
    test(4)
    test(5)
    test(6)
    test(1, ListNode(1)) # this will return a 'NoneType' object has no attribute 'next' exception since head is None
    test(2, ListNode(1))
    test(2, ListNode(1, ListNode(2)))

        

        