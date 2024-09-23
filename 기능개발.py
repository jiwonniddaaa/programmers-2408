from collections import deque

def solution(progresses, speeds):
    days = []
    
    # 각 작업이 완료되는 데 필요한 일수
    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        day = (100 - progress + speed - 1) // speed
        days.append(day)

    deployment_queue = deque()
    deployments = []
    
    # 함께 배포할 수 있는 작업 수
    for day in days:
        if not deployment_queue or day > deployment_queue[0]:
            if deployment_queue:
                deployments.append(len(deployment_queue))  # 대기 작업 수 추가
            # 모든 작업 제거
            deployment_queue.clear()
        deployment_queue.append(day)

    deployments.append(len(deployment_queue))  # 마지막 작업 추가
    return deployments