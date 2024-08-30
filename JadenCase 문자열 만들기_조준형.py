

def solution(s):
    
    word = s.split(' ')
    
    answer = ''
    for i in word:
        answer += i.capitalize() + ' '
    answer = answer[0:-1]
    return answer