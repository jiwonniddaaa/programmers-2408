def solution(n):
    # (n-1)칸 + 1칸 / (n-2)칸 + 2칸 => 피보나치 수열 이용
    
    # n이 1, 2일때 고려
    if n == 1 :
        return 1
    if n == 2 :
        return 2
    
    # 빈 리스트 생성
    f = [0] * (n + 1)
    # F[1], F[2]을 지정
    f[1] = 1
    f[2] = 2
    
    #2부터 돌면서 F[i]를 갱신, answer을 나머지값으로 업데이트
    for i in range(3, n + 1) :
        f[i] = (f[i - 1] + f[i - 2]) % 1234567
        
    return f[n]