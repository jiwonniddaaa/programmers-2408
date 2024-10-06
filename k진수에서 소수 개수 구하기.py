# 소수인지 판정
def is_prime(num) :
    if num < 2 :
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 :
            return False
    return True

def solution(n, k) :
    # n을 k진수로 변환
    number = "0123456789ABCDEF"
    k_n = ""
    
    if n == 0 :
        return 0
    
    while n > 0 :
        k_n = number[n % k] + k_n
        n //= k
    
    # 0으로 구분하여 나누기
    parts = k_n.split('0')
    prime_count = 0
    
    # 각 부분이 숫자일 경우에만 처리
    for part in parts :
        if part :
            num = int(part)  # 숫자로 변환
            if is_prime(num) :  # 소수인지 확인
                prime_count += 1
    
    return prime_count