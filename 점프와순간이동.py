def solution(n):
    ans = 0
    # 거꾸로 가는 방법 쓰기, 짝수면 반 나눠주고 홀수면 점프 추가
    while n >= 1 :
        while n % 2 == 0 :
            n /= 2
        n -= 1
        ans += 1
        
    return ans