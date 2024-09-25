def solution(clothes):
    # 옷 종류, 수로 딕셔너리 만듬
    dic = {}
    answer = 1
    
    for b,a in clothes:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1
            
    for i in list(dic.values()):
        # 조합 수 계산
        answer *= (i + 1)
    
    # 아무것도 입지않은 경우 제외
    answer -= 1
    
    return answer