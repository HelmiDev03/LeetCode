# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def fct(head,index):
            if  not head : 
                return 0
            return head.val * pow(2,index) + fct(head.next  , index  - 1 )    
        def getnbnodes(head):
            if not head : 
                return 0
            return  1 + getnbnodes(head.next)    
        return fct(head,getnbnodes(head) - 1)



