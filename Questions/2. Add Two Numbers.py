# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        new_head=ListNode(0)
        carry=0
        curr=new_head

        while l1 and l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            data=x+y+carry
            carry=data//10
            curr.next=ListNode(data%10)
            curr=curr.next

            if l1:
                l1=l1.next

            if l2:
                l2=l2.next
        if carry:
            curr.next=ListNode(carry)

        return new_head.next
