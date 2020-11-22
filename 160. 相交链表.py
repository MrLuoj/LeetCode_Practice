
# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p_A = headA
        p_B = headB

        while p_A != p_B:
            p_A = headB if p_A is None else p_A.next
            p_B = headA if p_B is None else p_B.next
        return p_A