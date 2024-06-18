# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            h = []
            for x in lists:
                pointer = x
                while pointer:
                    heappush(h, pointer.val)
                    pointer = pointer.next
            head = ListNode(0)
            cur = head
            while len(h) != 0:
                cur.next = ListNode(heappop(h))
                cur= cur.next
            return head.next