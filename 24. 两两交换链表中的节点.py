
# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11019/7-8-lines-C++-Python-Ruby

def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next