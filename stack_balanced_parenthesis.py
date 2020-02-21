"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""

from stack import Stack

def is_paren_match(p1, p2):
    if p1=='(' and p2==')':
        return True
    elif p1=='{' and p2=='}':
        return True
    elif p1=='[' and p2==']':
        return True
    else:
        return False        

def is_balanced_parenthesis(input_string):
    stack = Stack()
    is_balanced = True
    index = 0

    while index < len(input_string) and is_balanced==True:
        element = input_string[index]
        if element in "({[":
            stack.push(element)
        elif element in ")}]":
            if stack.is_empty():
                is_balanced = False
            else:
                top_element = stack.pop()
                if not is_paren_match(top_element, element):
                    is_balanced = False
        
        index += 1
    if stack.is_empty() and is_balanced==True:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_balanced_parenthesis("(w{wqed[asd]aaa}aasdaa)aaa"))
