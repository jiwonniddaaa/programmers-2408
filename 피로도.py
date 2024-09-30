# 실패함 ... 뭔지 잘 모르겟다

# 완전 탐색 : 모든 경우의 수 시도
def solution(k, dungeons):
    max_count = 0
    n = len(dungeons)

    # 방문 여부를 저장하는 리스트
    visited = [False] * n

    # 탐험 가능한 최대 던전 수를 계산하는 반복문
    for i in range(n):
        fatigue = k  # 초기 피로도
        count = 0  # 탐험 던전 수

        for j in range(n):
            for x in range(n):
                if not visited[x] and fatigue >= dungeons[x][0]:  # 최소 피로도 확인
                    visited[x] = True
                    fatigue -= dungeons[x][1]  # 소모 피로도 차감
                    count += 1

        # 탐험 후 최대 탐험 던전 수 갱신
        max_count = max(max_count, count)

    return max_count + 1