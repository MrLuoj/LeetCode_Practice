
# https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O%28n%29-time-O%281%29-space

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, slow, rev.next = slow, slow.next, rev
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return rev == None