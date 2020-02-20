
class Stack():
    def __init__(self, parent=None):
        self.item_list = []

    def push(self, item):
        self.item_list.append(item)

    def pop(self):
        return self.item_list.pop()

    def get_stack(self):
        return self.item_list

    def is_empty(self):
        return self.item_list == []

    def peek(self):
        if not self.is_empty():
            return self.item_list[-1]


if __name__ == "__main__":
    stack = Stack()
    print("is stack empty? - " + str(stack.is_empty()))
    stack.push('D')
    stack.push('S')
    stack.push('A')
    print(stack.get_stack())
    stack.pop()
    print(stack.get_stack())
    print("is stack empty? - " + str(stack.is_empty()))
    print("peek element is: " + str(stack.peek()))