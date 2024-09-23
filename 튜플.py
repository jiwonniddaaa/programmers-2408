def solution(s):
    
    # 빈 리스트 만들어 분리
    first = []
    
    for i in s.split("},") :
        first.append(i.strip("{}").split(","))
    
    # 원소 개수별로 정렬
    first.sort(key=len)
    
    answer = []
    
    # 리스트 돌면서 값 answer에 넣어주기
    for i in first :
        for j in i :
            if j not in answer :
                answer.append(j)
    
    # 출력
    return list(map(int, answer))