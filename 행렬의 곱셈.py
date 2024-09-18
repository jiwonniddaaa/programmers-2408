def solution(arr1, arr2):
    
    a = len(arr1)  # arr1의 행 개수
    b = len(arr1[0])  # arr1의 열 개수 (arr2의 행 개수와 같아야 함)
    c = len(arr2[0])  # arr2의 열 개수
    
    # 결과를 저장할 리스트 초기화 (행렬의 크기는 a x c)
    answer = [[0 for _ in range(c)] for _ in range(a)]
    
    for i in range(a):
        for j in range(c):
            for k in range(b):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer