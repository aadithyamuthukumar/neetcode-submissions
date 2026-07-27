class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0 and curr != self.tail:
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        
        newNode = ListNode(val)
        next = self.head.next
        prev = self.head

        newNode.prev = prev
        newNode.next = next
        next.prev = newNode
        prev.next = newNode


    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        next = self.tail
        prev = self.tail.prev

        newNode.prev = prev
        newNode.next = next
        next.prev = newNode
        prev.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        newNode = ListNode(val)

        while curr and index > 0:
            curr = curr.next
            index -=1
        

        if curr and index ==0:
            prev = curr.prev
            newNode.next = curr
            curr.prev = newNode
            newNode.prev = prev
            prev.next = newNode

        
    def deleteAtIndex(self, index: int) -> None:     
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -=1
        
        if  curr and index == 0 and curr != self.tail:
            next = curr.next
            prev = curr.prev
            prev.next = next
            next.prev = prev
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)