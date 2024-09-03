def solution(n):
    one_count = 0
    n_one_count = 0
    # n을 2진수로 변환했을 때 1의 개수 구하기
    one_count = bin(n)[2:].count('1')
    # while문으로 n+1부터 2진수로 변환하여 1의 개수 구하고 n의 1의 개수와 비교 -> 같으면 break
    while (one_count != n_one_count) :
        n += 1
        n_one_count = bin(n)[2:].count('1')
    answer = n
    return answer