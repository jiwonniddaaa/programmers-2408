from collections import Counter

def solution(k, tangerine):
    # 개수 세어주는 Counter 클래스 사용(역순)
    # 딕셔너리라서 sorted
    tangerine = sorted(Counter(tangerine).values(), reverse = True)
    sum = 0
    answer = 0
    # tangerine을 돌면서 합과 종류를 세어줌
    for i in tangerine :
        sum += i
        answer += 1
        # 합이 k에 도달하면 멈춤
        if sum >= k :
            break
    return answer