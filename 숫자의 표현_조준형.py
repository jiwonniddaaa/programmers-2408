def solution(n):
    
    answer = 0 # 정답의 횟수
    s = 1 # n을 분리하는 수
    
    # n = sum(s) + s*a (a는 0,1,2...)
    # n - sum(s) >= 0 양의정수 일때까지 count
    while n >= s*(s+1)/2:
        if (n-s*(s+1)/2) % s == 0:
            answer += 1
        s+=1
    return answer