# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next # store next node in temporary place
            curr.next = prev #make the curr node point to prec
            prev = curr #current becomes previous
            curr = temp #next node becomes temporary node
        return prev



        