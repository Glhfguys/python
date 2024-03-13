class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None 

    def length(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)
stack =Stack()
stack.push('T1')
stack.push('T2')
stack.push('T3')

print('stack:', stack)
print('stack.is_empty():', stack.is_empty())
print('stack.length():', stack.length())
print('stack.top():', stack.top())
print('stack.pop():', stack.pop())
print('stack:', stack)