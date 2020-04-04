class Stack:
  def __init__(self):
    self.stack = []
  def push(self, item):
    self.stack.append(item)
  def pop(self):
    return self.stack.pop()

# sample_stack = Stack()
# sample_stack.push(10)
# sample_stack.push(20)
# print(sample_stack.pop())
# print(sample_stack.pop())