# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        #m1- Length-Based Approach
        # length = 0
        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next
        # if length % 2 != 0:
        #     #odd
        #     target = math.ceil(length/2)
        # else:
        #     target = (length // 2)+1
        # curr = head
        # for _ in range(target - 1):
        #     curr = curr.next
        # return curr

        #m2- using slow,fast pointer
        slow,fast = head,head
        while fast and fast.next: #both non null
            slow = slow.next
            fast = fast.next.next
        return slow