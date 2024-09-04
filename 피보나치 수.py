def solution(n):
    
    # 빈 리스트 생성
    f = [0] * (n + 1)
    # F[1], F[2]을 지정
    f[1] = 1
    f[2] = 2
    
    #3부터 돌면서 F[i]를 갱신, answer을 나머지값으로 업데이트
    for i in range(3, n + 1) :
        f[i] = f[i - 1] + f[i - 2]
    
    answer = f[i] % 1234567
        
    return answer