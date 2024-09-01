def solution(s):
    #열린, 닫힌 괄호 정의
    open = 0
    close = 0
    
    #문자열 순회하며 괄호 수 세기
    for char in s :
        if char == '(' :
            open += 1
        elif char == ')' :
            close += 1
        #닫힌 괄호가 열린 괄호보다 크면 false
        if close > open :
            answer = False
            return answer
        
    #다 돌면 수가 같은지 확인    
    answer = (open == close)
    
    return answer