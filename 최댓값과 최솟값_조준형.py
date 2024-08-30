def solution(s):
    # 문자열을 공백 기준으로 나누어 리스트로 변환
    num = s.split()
    
    # 최소값과 최대값 찾기
    max_n = max(num)
    min_n = min(num)
    
    # "(최소값) (최대값)" 형식의 문자열로 반환
    return max_n, min_n