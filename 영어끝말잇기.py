def solution(n, words):
    # aword는 나온 단어들 리스트, 첫 단어 넣어주기
    aword = [words[0][0]]
    # enumerate는 인덱스 i, 요소 같이 출력
    for i, word in enumerate(words):
        # aword에 단어가 없거나, 마지막 글자랑 첫글자가 같으면 aword에 추가
        if word not in aword and aword[-1][-1] == word[0]:
            aword.append(word)
        # 아니면 탈락하는 사람 번호, 몇 번째 차례에 탈락하는지 출력
        else:
            return [i % n + 1, (i // n) + 1]
    # 전부 통과되면 0, 0 출력    
    return [0, 0]