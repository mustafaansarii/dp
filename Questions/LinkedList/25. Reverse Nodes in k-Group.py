# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        # Count total nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while count >= k:
            curr_head = curr
            prev.next = None

            # Reverse k nodes
            prev_node = None
            for _ in range(k):
                next_node = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = next_node

            # Connect with rest of the list
            prev.next = prev_node
            curr_head.next = curr
            prev = curr_head
            count -= k

        return dummy.next

    def revers(self, node, k):
        if not node:
            return None

        # Check if k nodes exist
        count = 0
        curr = node
        while curr and count < k:
            count += 1
            curr = curr.next

        if count < k:
            return node

        prev = None
        curr = node
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        node.next = curr
        return prev