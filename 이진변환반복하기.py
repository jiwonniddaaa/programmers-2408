def solution(s):
    n = 0
    r = 0

    while s != '1':
        # '0' 제거 및 제거된 '0'의 개수를 r에 추가
        r += s.count('0')
        s = s.replace('0', '') # '0'을 제거한 새 문자열로 업데이트
        
        # 문자열의 길이를 이진수로 변환
        s = bin(len(s))[2:]  # '0b' 접두사를 제거하기 위해 [2:] 슬라이싱
        n += 1  # 변환 횟수 증가
    
    answer = [n, r]           
    
    return answer