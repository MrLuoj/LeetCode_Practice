
# https://leetcode.com/problems/reverse-linked-list/discuss/58338/Python-solution-Simple-Iterative

def reverseList(self, head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev