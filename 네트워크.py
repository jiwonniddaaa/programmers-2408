def solution(n, computers):
    def dfs(i, visited):
        # 현재 방문
        visited[i] = True
        
        # i와 연결된 컴퓨터 방문
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j, visited)
    
    visited = [False] * n  
    answer = 0  
    
    for i in range(n):
        if not visited[i]:  
            dfs(i, visited) 
            answer += 1
    
    return answer