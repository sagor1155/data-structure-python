from stack import Stack

def reverse_string(input_string):
    stack = Stack()
    for elements in input_string:
        stack.push(elements)

    output_str = ""
    while not stack.is_empty():
        output_str += stack.pop()

    return output_str


print(reverse_string("qwerty"))    