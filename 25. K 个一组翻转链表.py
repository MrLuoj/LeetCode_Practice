
# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/172576/Python-or-Follow-up-of-LC206

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, pre = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return pre


    def reverse(self, head, count):
        pre, cur = None, head
        while count > 0:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            count -= 1
        return (cur, pre)