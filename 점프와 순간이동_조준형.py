def solution(N):
    ans = 0
    
    while True:
        if N == 1:
            ans += 1
            break
        elif N % 2 ==1:
            N -= 1
            ans += 1
        else:
            N /= 2
        

    return ans