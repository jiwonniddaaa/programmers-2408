def solution(s):
    
    a = 0 #이진변환 반복횟수
    n = 0 #0의 갯수
    
    while s != '1':
        #0의 갯수 세주기
        n += s.count('0')
        
        #0제거 후 이진변환
        s = bin(len(s.replace('0','')))[2:]
        a += 1
    return [a, n]