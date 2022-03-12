# 10 min, 1211 ms	16.9 MB
class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val < min:
            self.min = val
        if val > max:
            self.max = val

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            return
        self.stack = self.stack[:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        min = 2 ** 31
        for val in self.stack:
            if val < min:
                min = val
        return min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()