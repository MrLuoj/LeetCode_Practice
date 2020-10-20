
# https://leetcode-cn.com/problems/linked-list-cycle/solution/141-linked-list-cycle_li-jie-by-gulugulu_go/

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        # if not head��  # û��Ҫ����д���Լ���whileѭ���жϸ����
        #     return False

        while fast and fast.next:  # ��ֹheadΪ�պͳ��ֿ�ָ���next�����
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False

