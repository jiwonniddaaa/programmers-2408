def solution(elements) :
    circle = elements * 2  # 원형 수열 - 배열*2
    answer = set()  # 중복을 허용하지 않는 자료구조 set

    for n in range(1, len(elements) + 1) :
        for i in range(len(elements)) :
            subarray = sum(circle[i:i + n])  # 부분수열
            answer.add(subarray)

    
    return len(answer)