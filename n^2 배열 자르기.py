def solution(n, left, right):
    answer = []
    
    # left부터 right까지 반복하면서 값을 계산
    for i in range(left, right + 1):
        # i // n : 행, i % n : 열
        value = max(i // n, i % n) + 1
        answer.append(value)
    
    return answer