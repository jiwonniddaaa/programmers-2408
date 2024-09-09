import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    # 배열의 첫 번째 요소로 초기화
    result = arr[0]
    
    # for문으로 두 번째 요소부터 lcm계산
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    
    return result