def solution(n):
    answer = 0
    m = 1
    
    while True:
        # m개의 연속된 자연수의 합 = n
        # 식의 값이 0보다 작으면 k는 음수, 음/양을 따지므로 분모 없애기
        if ((2 * n) - m * (m - 1)) <= 0:
            break
        
        # k가 자연수이려면 나누어 떨어져야 함
        if ((2 * n) - m * (m - 1)) % (2 * m) == 0:
            answer += 1
        
        m += 1
    return answer