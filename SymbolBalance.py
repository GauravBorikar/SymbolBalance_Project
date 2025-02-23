import re
from collections import deque

class SymbolBalance:
    def __init__(self):
        self.expression = ""
        self.cleaned_expression = ""

    def parseInput(self):
        """
        Accepts user input, removes comments, and extra spaces.
        """
        self.expression = input("Enter the expression: ")
        self.cleaned_expression = re.sub(r'/.*?/', '', self.expression).strip()
        return self.cleaned_expression

    def checkSyntax(self):
        """
        Checks for balanced symbols { }, [ ], ( ), and /* */.
        """
        stack = deque()
        pairs = {'}': '{', ']': '[', ')': '('}
        
        for i, char in enumerate(self.cleaned_expression):
            if char in "{[(" :
                stack.append(char)
            elif char in "}])":
                if not stack:
                    return f"Error2: EmptyStack error, missing opening symbol for {char} at position {i}"
                top = stack.pop()
                if pairs[char] != top:
                    return f"Error3: Mismatch error, {char} does not match {top} at position {i}"
        
        if stack:
            return f"Error1: NonEmptyStack error, unmatched {stack[-1]} left in stack"
        
        return "Symbol Balanced"

    def postfixExpress(self):
        """
        Converts infix expression to postfix if balanced.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, '{': 0, '[': 0}
        output = []
        stack = deque()
        tokens = re.findall(r'\w+|[+\-*/(){}\[\]]', self.cleaned_expression)
        
        for token in tokens:
            if token.isalnum():
                output.append(token)
            elif token in "({[":
                stack.append(token)
            elif token in ")}]":
                while stack and stack[-1] not in "({[":
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                    output.append(stack.pop())
                stack.append(token)
        
        while stack:
            output.append(stack.pop())
        
        return " ".join(output)

if __name__ == "__main__":
    sb = SymbolBalance()
    sb.parseInput()
    syntax_result = sb.checkSyntax()
    print(syntax_result)
    if syntax_result == "Symbol Balanced":
        print("Postfix Expression:", sb.postfixExpress())
