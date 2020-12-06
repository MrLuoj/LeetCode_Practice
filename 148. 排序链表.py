
# https://leetcode.com/problems/sort-list/discuss/46711/Python-easy-to-understand-merge-sort-solution

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(start)
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = p = ListNode(0)
        while l and r:
            if not l:
                return r
            if not r:
                return l
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next