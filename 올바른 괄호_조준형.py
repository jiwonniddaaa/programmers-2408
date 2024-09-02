def solution(s):
    answer = 0
    ans_list = list(s)
    for i in ans_list:
        if i == '(':
            answer += 1
        elif i == ')':
            answer -= 1
            if answer < 0:
                return False  # 여기에서 바로 False를 반환하고 종료합니다.
    if answer == 0:
        return True
    else:
        return False