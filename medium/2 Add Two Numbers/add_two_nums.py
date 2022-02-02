# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.getNumber(l1)
        num2 = self.getNumber(l2)
        numsum = num1 + num2
        ln = self.intToReversedLinkedList(numsum) # 708
        return ln
        
    
    def getNumber(self, l1: ListNode) -> int:
        ''' Reverses a Linked List using a Stack'''
        stack = []
        # add initial value to stack
        stack.append(l1.val)
        nextNode = l1.next
        place = 10
        # go through nodes until there are none left
        while(nextNode is not None):
            stack.append(nextNode.val * place)
            nextNode = nextNode.next
            # make sure the 10's place is accurately recorded
            place = place * 10
            
        # convert the stack to an int in the correct order
        number = 0
        while(len(stack) > 0):
            number = number + stack.pop()
        
        return number
            
            
    def intToReversedLinkedList(self, val: int) -> ListNode:
        '''Converts an int to a reversed Linked List'''
        # for val 708, will return a  with 807
        numStr = str(val) 
        nextNode = None
        for i in range(0, len(numStr)):
            linked_list_val = int(numStr[i])
            ln = ListNode(linked_list_val, nextNode)
            nextNode = ln
        
        return nextNode
            
        
        
        
        