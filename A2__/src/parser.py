from src.astDefiner import *
from src.lexer import *

class Parser:
    def __init__(self, tokens):
        # We first initialize the parser with the list of tokens, the current index and an empty stack
        self.tokens = tokens
        self.i = 0
        self.stack = []

    def parse(self):
        # This function is used to parse the tokens
        try:
            while self.i < len(self.tokens): # We iterate over the tokens
                token = self.tokens[self.i] # We get the current token
                if isinstance(token, StringToken): # If the token is a StringToken
                    self.stack.append(token.v) # We append the value of the token to the stack
                elif isinstance(token, NumberToken): # If the token is a NumberToken
                    self.stack.append(int(token.v)) # We append the value of the token to the stack
                elif isinstance(token, NegNumberToken): # If the token is a NegNumberToken
                    self.stack.append(-int(token.v)) # We append the value of the token to the stack
                elif isinstance(token, DecimalNumberToken): # If the token is a DecimalNumberToken
                    self.stack.append(float(token.v)) # We append the value of the token to the stack
                elif isinstance(token, NegDecimalNumberToken):  # If the token is a NegDecimalNumberToken
                    self.stack.append(-float(token.v)) # We append the value of the token to the stack
                elif isinstance(token, WordToken): # If the token is a WordToken
                    if token.v == '+': # If the token is a plus sign
                        assert len(self.stack) > 1, "EMPTY STACK" # We check if the stack has more than one element
                        num1 = self.stack.pop() # We pop the last element of the stack
                        num2 = self.stack.pop()
                        assert type(num1) == int or type(num1) == float, "INVALID OPERAND TYPE" # We check if the type of the element is int or float
                        assert type(num2) == int or type(num2) == float, "INVALID OPERAND TYPE"
                        self.stack.append(num1 + num2) # We append the sum of the two elements to the stack
                    elif token.v == '-': # If the token is a minus sign
                        assert len(self.stack) > 1, "EMPTY STACK" # We check if the stack has more than one element
                        num1 = self.stack.pop() # We pop the last element of the stack
                        num2 = self.stack.pop()
                        assert type(num1) == int or type(num1) == float, "INVALID OPERAND TYPE" # We check if the type of the element is int or float
                        assert type(num2) == int or type(num2) == float, "INVALID OPERAND TYPE"
                        self.stack.append(num2 - num1) # We append the difference of the two elements to the stack
                    elif token.v == '*': # If the token is a multiplication sign
                        assert len(self.stack) > 1, "EMPTY STACK" # We check if the stack has more than one element
                        num1 = self.stack.pop() # We pop the last element of the stack
                        num2 = self.stack.pop()
                        assert type(num1) == int or type(num1) == float, "INVALID OPERAND TYPE" # We check if the type of the element is int or float
                        assert type(num2) == int or type(num2) == float, "INVALID OPERAND TYPE"
                        self.stack.append(num1 * num2) # We append the product of the two elements to the stack
                    elif token.v == '/': # If the token is a division sign
                        assert len(self.stack) > 1, "EMPTY STACK" # We check if the stack has more than one element
                        num1 = self.stack.pop() # We pop the last element of the stack
                        num2 = self.stack.pop()
                        assert type(num1) == int or type(num1) == float, "INVALID OPERAND TYPE" # We check if the type of the element is int or float
                        assert type(num2) == int or type(num2) == float, "INVALID OPERAND TYPE"
                        assert num1 != 0, "DIV BY ZERO" # We check if the divisor is not zero
                        self.stack.append(num2 / num1) # We append the division of the two elements to the stack
                    elif token.v == '^': # If the token is a power sign
                        assert len(self.stack) > 1, "EMPTY STACK" # We check if the stack has more than one element
                        num1 = self.stack.pop() # We pop the last element of the stack
                        num2 = self.stack.pop()
                        assert type(num1) == int or type(num1) == float, "INVALID OPERAND TYPE" # We check if the type of the element is int or float
                        assert type(num2) == int or type(num2) == float, "INVALID OPERAND TYPE"
                        assert not(num1 <= 0 and num2 == 0), "DIV BY ZERO" # We check if the base is positive
                        self.stack.append(num2 ** num1) # We append the power of the two elements to the stack
                    elif token.v == 'get': # If the token is a get sign
                        inp_val = input() # We take the input from the user
                        if inp_val[0]!='"': # If the input is not a string
                            if inp_val[0] == "-": # If the input is a negative number
                                inp_val_wo_neg = inp_val[1:] # We remove the negative sign
                                if inp_val_wo_neg.isdigit(): # If the input is a digit
                                    self.stack.append(int(inp_val)) # We append the input to the stack
                                elif inp_val_wo_neg.replace('.', '', 1).isdigit(): # If the input is a decimal number
                                    self.stack.append(float(inp_val)) # We append the input to the stack
                                else: # If the input is not a number
                                    raise Exception(f"Input of Invalid type: {inp_val}") # We raise an exception
                            elif inp_val.isdigit(): # If the input is a digit
                                self.stack.append(int(inp_val)) # We append the input to the stack
                            elif inp_val.replace('.', '', 1).isdigit(): # If the input is a decimal number
                                self.stack.append(float(inp_val)) # We append the input to the stack
                            else: # If the input is not a number
                                raise Exception(f"Input of Invalid type: {inp_val}") # We raise an exception
                        else: # If the input is a string
                            if inp_val[-1] == '"': # If the input is a string
                                for i in range(1, len(inp_val)-1): # We iterate over the input
                                    if inp_val[i] == '"' and inp_val[i-1] != '\\': # If the input is a string and not an escape character, that is a discontinuity
                                        raise Exception(f"Invalid string: {inp_val}") # We raise an exception
                                self.stack.append(inp_val[1:-1]) # We append the input to the stack
                            else:
                                raise Exception(f"Invalid string: {inp_val}") # We raise an exception

                    elif token.v == 'put': # If the token is a put word
                        assert len(self.stack) > 0, "EMPTY STACK" # We check if the stack is not empty
                        def format_value(value): # If it is not a string, we format it
                            if isinstance(value, str):  # Format strings
                                return '"' + value + '"' # Format string values
                            else:  # Format numbers or other types
                                return str(value) # Format other types
                        print(format_value(self.stack[-1])) # We print the last element of the stack
                        # print(self.stack[-1]) # We print the last element of the stack
                        self.stack.pop() # We pop the last element of the stack
                    elif token.v == 'print': # Same as put for strings, without the quotes
                        assert len(self.stack) > 0, "EMPTY STACK"
                        assert type(self.stack[-1]) == str, "INVALID OPERAND TYPE"
                        to_print = self.stack[-1]
                        if '\\n' in to_print:
                            to_print = to_print.replace('\\n', '\n')
                        if '\\t' in to_print:
                            to_print = to_print.replace('\\t', '\t')
                        if '\\\\' in to_print:
                            to_print = to_print.replace('\\\\', '\\')
                        if '\\"' in to_print:
                            to_print = to_print.replace('\\"', '"')
                        print(to_print)
                        self.stack.pop()
                    elif token.v == 'pop': # If the token is a pop word
                        assert len(self.stack) > 0, "EMPTY STACK" # We check if the stack is not empty
                        self.stack.pop() # We pop the last element of the stack
                    elif token.v == 'dup': # If the token is a dup word
                        assert len(self.stack) > 0, "EMPTY STACK" # We check if the stack is not empty
                        self.stack.append(self.stack[-1]) # We append the last element of the stack to the stack
                    elif token.v == 'rot': # If the token is a rot word
                        assert len(self.stack) > 1, "EMPTY STACK" # We check if the stack has more than one element
                        num1 = self.stack.pop() # We pop the last element of the stack
                        num2 = self.stack.pop() # We pop the second last element of the stack
                        self.stack.append(num1) # We append the last element of the stack to the stack
                        self.stack.append(num2) # We append the second last element of the stack to the stack
                    elif token.v == 'concat': # If the token is a concat word
                        assert len(self.stack) > 1, "EMPTY STACK" # We check if the stack has more than one element
                        assert type(self.stack[-1]) == str, "INVALID OPERAND TYPE" # We check if the last element of the stack is a string
                        assert type(self.stack[-2]) == str, "INVALID OPERAND TYPE" # We check if the second last element of the stack is a string
                        stri1 = self.stack.pop() # We pop the last element of the stack
                        stri2 = self.stack.pop() # We pop the second last element of the stack
                        self.stack.append(stri2 + stri1) # We append the concatenation of the two strings to the stack
                    else: # If the token is not a known word
                        raise Exception(f"Unknown token: {token.v}") # We raise an exception
                self.i += 1 # We increment the index
        except Exception as e: # If an exception is raised
            print(e)