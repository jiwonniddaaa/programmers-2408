def solution(n,a,b):
    answer = 0
    
    # 각 (번호 + 1) // 2 의 몫이 몇번째 대진인지 나타냄, 같으면 같은 대진
    while a != b :
        a = (a + 1) // 2 
        b = (b + 1) // 2
        answer += 1

    return answer