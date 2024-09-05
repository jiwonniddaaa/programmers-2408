def solution(brown, yellow):
    x = 0
    y = 0
    if yellow == 1 :
        return [3, 3]
    for i in range(yellow // 2 + 1, 1, -1) :
        if (yellow % i) == 0 :
            x = i
            y = yellow // i
            
            # 전체 카펫의 넓이에서 yellow의 넓이를 제외한 나머지가 brown과 같은지 확인
            if (x + 2) * (y + 2) == brown + yellow:
                return [x + 2, y + 2]