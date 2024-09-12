def is_valid(s):
    stack = []
    bracket = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != bracket[char]:
                return False
            stack.pop()
    
    return not stack

def solution(s):
    count = 0
    n = len(s)
    
    for i in range(n):
        rotated_s = s[i:] + s[:i]
        if is_valid(rotated_s):
            count += 1
    
    return count
