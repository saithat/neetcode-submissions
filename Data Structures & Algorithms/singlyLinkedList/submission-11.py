class ListNode:
    def __init__(self, val: int = None):
        self.value = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.head:
            cur = self.head
            for i in range(index):
                if (cur):
                    cur = cur.next
                else:
                    return -1
            return cur.value if cur else -1
        return -1

    def insertHead(self, val: int) -> None:
        tmp = ListNode(val)
        tmp.next = self.head
        self.head = tmp
        if not self.tail:
            self.tail = tmp

    def insertTail(self, val: int) -> None:
        tmp = ListNode(val)
        if self.tail:
            self.tail.next = tmp

            self.tail = tmp
        else:
            self.tail = tmp
            self.head = tmp

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            return True
            
        cur = self.head
        prev = None
        for i in range(index):
            if (cur.next):
                prev = cur
                cur = cur.next
            else:
                return False
        
        prev.next = cur.next
        if cur == self.tail:
            self.tail = prev
        return True  

    def getValues(self) -> List[int]:
        cur = self.head
        vals = []
        while (cur):
            vals.append(cur.value)
            cur = cur.next
        return vals