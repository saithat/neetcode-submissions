class MinStack:

    def __init__(self):
        self.stack = []
        self.stackLen = 0
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stackLen += 1
        if self.minStack:
            if self.minStack[-1] >= val:
                self.minStack.append(val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.stackLen -= 1
        if self.minStack[-1] == val:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
