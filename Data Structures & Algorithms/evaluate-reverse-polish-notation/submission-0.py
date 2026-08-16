class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []
        for each in tokens:
            if each not in ops:
                stack.append(int(each))
            else:
                second = stack.pop()
                first = stack.pop()
                if each == "+":
                    res = first + second
                elif each == "-":
                    res = first - second
                elif each == "*":
                    res = first * second
                elif each == "/":
                    res = int(first/second)
                stack.append(res)
        
        return stack[-1]
                    
        