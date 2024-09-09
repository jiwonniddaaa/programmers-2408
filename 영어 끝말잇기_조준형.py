def solution(n, words):
    answer = [words[0]]

    for i in range(1,len(words)):
        
        if words[i][0] != words[i-1][-1] or words[i] in answer:
            return [i%n+1, i//n +1] 
            # (i+1 -1)%n + 1 ,123123
            # (i+1 -1)//n +1 , 111222333
        
        answer.append(words[i])

    return [0,0]