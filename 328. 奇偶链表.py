
# https://leetcode.com/problems/odd-even-linked-list/discuss/78095/Clear-Python-Solution

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)

        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next