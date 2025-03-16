# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head=ListNode(0)
        new_head=head
        while list1 and list2:
            if list1.val<=list2.val:
                new_head.next=list1
                list1=list1.next
            else:
                new_head.next=list2
                list2=list2.next
            new_head=new_head.next
        if list1:
            new_head.next=list1
        if list2:
            new_head.next=list2
        return  head.next