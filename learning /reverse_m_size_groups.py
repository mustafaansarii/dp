# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
def reverse_m_size_groups(head, M):
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count += 1
    prev = None
    curr = head
    temp_head = head
    prev_tail = None
    while count >= M:
        next_head = temp_head
        for _ in range(M):
            next_head = next_head.next

        prev = None
        curr = temp_head
        for _ in range(M):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if prev_tail:
            prev_tail.next = prev
        else:
            head = prev

        temp_head.next = next_head
        prev_tail = temp_head
        temp_head = next_head
        count -= M

    return head
