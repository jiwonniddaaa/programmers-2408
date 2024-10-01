# 너비우선탐색(BFS)는 하나의 요소를 방문하고 그 요소에 인접한 모든 요소를 우선 방문하는 방식
# 깊이우선탐색(DFS)는 트리의 한 요소(노드)와 다음 수준(level)의 자식 노드를 따라가는 방향으로 탐색하는 방식

from collections import deque

def solution(numbers, target):
    # BFS 탐색을 위한 큐 (현재 합, 현재 인덱스를 저장)
    queue = deque([(0, 0)])  # (current_sum, index)
    answer = 0
    
    # 큐가 빌 때까지 탐색
    while queue:
        current_sum, index = queue.popleft()
        
        # 모든 숫자를 처리했을 때
        if index == len(numbers):
            # 현재 합이 목표 값과 같으면 경우의 수 증가
            if current_sum == target:
                answer += 1
        else:
            # 현재 인덱스의 숫자를 더하거나 빼는 두 가지 경우를 큐에 추가
            queue.append((current_sum + numbers[index], index + 1))
            queue.append((current_sum - numbers[index], index + 1))
    
    return answer