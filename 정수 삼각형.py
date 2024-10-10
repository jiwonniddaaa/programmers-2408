def solution(triangle):
    # 아래 -> 위
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(row + 1):
            # 위 두 숫자 중 큰 거 더해서 업데이트
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    answer = triangle[0][0]
    return answer