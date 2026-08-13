class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        numStack = []


        total = 0
        for token in tokens:
            
            if token == '+':
                numStack.append(numStack.pop() + numStack.pop())
            elif token == "*":
                numStack.append(numStack.pop() * numStack.pop())
            elif token == '/':
                a, b = numStack.pop(), numStack.pop()
                numStack.append(int(b/a))
            elif token == "-":
                a, b = numStack.pop(), numStack.pop()
                numStack.append(int(b - a))
            else:
                numStack.append(int(token))
        return numStack[0]

