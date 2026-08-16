class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs =  {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for each in s:
            if each in pairs:
                if len(stack) <= 0:
                    return False
                if stack[-1] != pairs[each]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(each)
        
        return len(stack) == 0
