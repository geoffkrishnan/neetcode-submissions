# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i, j = 0, 0
        node = head
        while node is not None:
            node = node.next
            i += 1
        l = (i // 2)
        nodej = head

        while nodej is not None and j < l:
            nodej = nodej.next
            j += 1

        return nodej
        

        