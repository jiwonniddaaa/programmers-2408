from collections import Counter

def make_pairs(s):
    pairs = []
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        # 두 글자가 모두 알파벳인지 확인(알파벳만 유효)
        if pair[0].isalpha() and pair[1].isalpha():
            pairs.append(pair)
    return pairs

def solution(str1, str2):
    # 1. 대소문자 통일
    str1 = str1.lower()
    str2 = str2.lower()

    # 2. 문자열을 2개씩 끊음
    pairs1 = make_pairs(str1)
    pairs2 = make_pairs(str2)

    # 3. 2개씩 끊은 부분집합의 개수 세기(다중집합 고려)
    counter1 = Counter(pairs1)
    counter2 = Counter(pairs2)

    # 4. 교집합, 합집합 계산
    # 교집합
    intersection = sum((counter1 & counter2).values())
    # 합집합
    union = sum((counter1 | counter2).values())

    # 5. 자카드 유사도 계산
    if union == 0:  # 합집합이 0이면 유사도는 1로 처리
        return 65536

    answer = int((intersection / union) * 65536)
    return answer


# 대소문자 통일
# 문자열을 2개씩 끊음
# 집합 사이 같은 원소를 찾음
# 교집합, 합집합 계산
# 교집합 / 합집합 * 65536
# 소수점 버리기 후 출력