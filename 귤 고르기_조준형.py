def solution(k, tangerine):
    # 1. 귤의 크기별 빈도 세기
    size_count = {}
    for size in tangerine:
        if size in size_count:
            size_count[size] += 1
        else:
            size_count[size] = 1
    
    # 2. 빈도 기준으로 내림차순 정렬
    sorted_count = sorted(size_count.values(), reverse=True)
    
    # 3. k개의 귤을 고를 때 크기 종류의 최소화
    types = 0
    for count in sorted_count:
        k -= count
        types += 1
        if k <= 0:
            break
    
    return types
