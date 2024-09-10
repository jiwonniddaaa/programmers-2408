def solution(s):
    def is_valid(s):
        #괄호 확인 위해 스택에 집어넣다 빼는 방법 사용
        stack = []
        # 괄호 짝 딕셔너리에 저장
        pair = {')': '(', ']': '[', '}': '{'}
        #문자열을 돌며 열린괄호면 append, 닫힌 괄호면 스택이 비어있지 않고 열린괄호 짝이 있는지 찾기
        for char in s:
            if char in pair.values():
                stack.append(char)
            elif char in pair.keys():
                if stack and stack[-1] == pair[char]:
                    stack.pop()
                else:
                    return False
        return not stack

    answer = 0
    for i in range(len(s)):
        # 괄호 회전 구현
        rotated_s = s[i:] + s[:i]
        if is_valid(rotated_s):
            answer += 1

    return answer