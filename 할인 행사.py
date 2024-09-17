def solution(want, number, discount):
    # 회원 등록 날짜 수
    member_days = 0

    for i in range(len(discount) - 9):  # i~i+10일간 할인 목록
        is_valid = True
        
        # want-number 모두 충족 확인
        for j in range(len(want)):
            # want[i]가 discount에 몇번 나오는지 확인
            if discount[i:i + 10].count(want[j]) < number[j]:
                is_valid = False
                break
        
        if is_valid:
            member_days += 1
    
    return member_days