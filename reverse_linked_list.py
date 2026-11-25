# LeetCode 206: Reverse Linked List
# ListNode is provided by the LeetCode judge.
class Solution:
    def reverseList(self, head):
        previous, current = None, head
        while current:
            following = current.next
            current.next = previous
            previous, current = current, following
        return previous
