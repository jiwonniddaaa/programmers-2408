def F(n):

    a = 0
    b = 1

    for i in range(n-1):
        a, b = b, a+b   # 숫자를 동시에 바꿔주기

    return b

def solution(n):
    return F(n)%1234567



