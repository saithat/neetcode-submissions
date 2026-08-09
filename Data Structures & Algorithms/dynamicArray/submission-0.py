class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.size = 0
        self.maxSize = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if (self.size >= self.maxSize):
            self.resize()
        self.arr[self.size] = n
        self.size += 1
        
    def popback(self) -> int:
        tmp = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -= 1
        return tmp

    def resize(self) -> None:
        self.maxSize *= 2
        newArr = [None] * (self.maxSize)
        for i, n in enumerate(self.arr):
            newArr[i] = n
        self.arr = newArr

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.maxSize