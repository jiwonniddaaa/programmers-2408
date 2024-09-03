#리스트 방식(효율성 테스트 통과 x)

def solution(s):
    s = list(s)
    i = 0
    while i < len(s) - 1 :
        if s[i] == s[i + 1] :
            del s[i:i+2]
            # 인덱스를 한 칸 뒤로 조정하지만, 리스트 길이에 따라 조정
            i = max(i - 1, 0)
        else :
            i += 1
            
    if len(s) == 0 :
        answer = 1
    else :
        answer = 0
    

    return answer

#스택 방식
def solution(s):
    # 빈 스택 만들어주기
    stack = []
    
    # 문자열 루프돌기
    for char in s:
        # 스택이 비지않고 & 스택 맨위와 현재 char 같으면 pop
        if stack and stack[-1] == char:
            stack.pop()
        # 스택 비어있으면 char을 추가
        else:
            stack.append(char)
    
    # 다 돌았는데 남아있으면 0
    if not stack :
        answer = 1
    else : answer = 0
    

    return answer