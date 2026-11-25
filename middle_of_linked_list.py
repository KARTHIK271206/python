# LeetCode 876: Middle of the Linked List
# ListNode is provided by the LeetCode judge.
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow
