"""
Use a stack data structure to convert integer values to their corresponding binary representation.
Example : 242
242 / 2 = 121 -> 0
121 / 2 = 60  -> 1
60 / 2  = 30  -> 0
30 / 2  = 15  -> 0
15 / 2  = 7   -> 1
7 / 2 = 3     -> 1
3 / 2 = 1     -> 1
1 / 2 = 0	  -> 1
"""

from stack import Stack

def convert_integer_to_binary(decimal_number):
    if decimal_number==0:
        return 0
    
    stack = Stack()
    while decimal_number > 0:
        remainder = decimal_number % 2 
        stack.push(remainder)
        decimal_number = decimal_number // 2    ## discards fractional part 

    bin_number = ""
    while not stack.is_empty():
        bin_number += str(stack.pop())

    return bin_number

print(convert_integer_to_binary(242))