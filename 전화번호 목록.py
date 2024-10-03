def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        # 현재 번호 길이만큼 다음 인덱스 번호 슬라이싱
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    
    return True