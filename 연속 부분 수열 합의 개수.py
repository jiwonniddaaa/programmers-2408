def solution(elements):
    n = len(elements)
    elements = elements * 2  # 원형 수열을 처리하기 위해 두 번 반복한 리스트 생성
    possible_sums = set()  # 중복을 방지하기 위해 set 사용

    # 길이가 1부터 n까지의 모든 부분 수열의 합 계산
    for length in range(1, n+1):
        for i in range(n):  # 시작 인덱스
            possible_sums.add(sum(elements[i:i+length]))  # 길이가 length인 부분 수열의 합 계산

    return len(possible_sums) 