"""
Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
########## correct but stupid ass solution, use two stacks and write good solution
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.value = []

    def push(self, x: int) -> None:
        self.value.append(x)

    def pop(self) -> None:
        self.value = self.value[:-1]

    def top(self) -> int:
        return self.value[-1]

    def getMin(self) -> int:
        return min(self.value)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()