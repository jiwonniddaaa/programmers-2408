def solution(citations):
    citations.sort(reverse=True)
    for i, value in enumerate(citations):
        if i >= value :
            return i
    return len(citations)