def glc(a, b):
    s = a*b
    while b != 0:
        a, b = b, a % b
    return s/a


def solution(arr):
    a= arr[0]
    for i in range(1,len(arr)):
        a = glc(a, arr[i])
    return a