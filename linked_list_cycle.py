# LeetCode 141: Linked List Cycle
# ListNode is provided by the LeetCode judge.
class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast: return True
        return False
