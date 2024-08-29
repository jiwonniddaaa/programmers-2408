##최댓값과 최솟값
def solution(s):
    #split하고 int로 변환, 여러 개 한번에 할 때 map 씀
    r = list(map(int, s.split()))
    #최대 최소 구하기
    min_v = min(r)
    max_v = max(r)
    #다시 문자열로 변환해서 공백 넣어주기
    answer = str(min_v) + " " + str(max_v)
    return answer

##최솟값 구하기
def solution(A,B):
    #배열이므로 정렬
    A.sort()
    B.sort()
    n = 0
    #배열 길이만큼 반복
    for i in range(len(A)) :
        #정렬된 배열이므로 최솟값*최댓값
        n = n + A[i]*B[-(i+1)]
    answer = n
    return answer

##JadenCase 문자열 만들기

def solution(s):
    #공백 연속 포함 조건으로 split에 공백 추가
    s = s.split(" ")
    for i in range(len(s)):
        #맨 앞글자만 대문자, 나머지 소문자 해주는 내장함수
        s[i] = s[i].capitalize()
    #문자열로 리스트 결합
    answer = " ".join(s)
    return answer