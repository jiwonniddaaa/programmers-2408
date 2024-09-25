# LRU : 가장 오랫동안 참조되지않은 페이지 교체
def solution(cacheSize, cities) :
    # 캐시사이즈가 0이면 모두 미스여서 *5
    if cacheSize == 0 :
        return len(cities) * 5
    
    cache = []
    answer = 0
    
    for i in cities :
        i = i.lower()
        # 스택에 있으면 
        if i in cache :
            cache.remove(i)
            cache.append(i)
            answer += 1
        # 스택에 없으면
        else :
            if len(cache) >= cacheSize :
                cache.pop(0)
            cache.append(i)
            answer += 5
            
    return answer