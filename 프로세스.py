def solution(priorities, location):
    # 우선순위-인덱스 리스트
    queue = [(priority, index) for index, priority in enumerate(priorities)]
    
    # 실행된 프로세스 수
    answer = 0
    
    while queue:
        current = queue.pop(0)
        
        # 우선순위 비교
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            answer += 1
            # 실행된 프로세스 = location이면 반환
            if current[1] == location:
                return answer