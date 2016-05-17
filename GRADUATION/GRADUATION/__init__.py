# GRADUATION
# Jaekyoung Kim (rlakim5521@naver.com)

def bitCount(n):
    ret = 0
    while(n != 0):
        if (n & 1) == 1:
            ret = ret + 1
        n = (n >> 1)
    return ret

def graduate(semester, taken):
    if(bitCount(taken) >= k): return 0
    if(semester == m): return 99
    if(cache[semester][taken] != -1): return cache[semester][taken]
    ret = 99
    canTake = (classes[semester] & ~taken)
    for i in xrange(n):
        if (canTake & (1 << i)) and (taken & prerequisite[i]) != prerequisite[i]:
            canTake = canTake & ~(1 << i)
    take = canTake
    while(take > 0):
        if(bitCount(take)>l):
            take = ((take - 1) & canTake)
            continue
        ret = min(ret, graduate(semester + 1, taken | take) + 1)
        take = ((take - 1) & canTake)
    ret = min(ret, graduate(semester + 1, taken))
    return ret

# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        # Input
        prerequisite = []
        classes = []
        n, k, m, l = map(int, raw_input().split())
        cache = [[-1 for _ in xrange(1 << n)] for _ in xrange(m)]
        for _ in xrange(n):
            pres = map(int, raw_input().split())
            new = 0
            for pre in pres[1:]:
                new = (new | (1 << pre))
            prerequisite.append(new)
        for _ in xrange(m):
            subjects = map(int, raw_input().split())
            new = 0
            for subject in subjects[1:]:
                new = (new | (1 << subject))
            classes.append(new)
    
        # Output
        ret = graduate(0, 0)
        if ret <= m:
            print ret
        else:
            print "IMPOSSIBLE"
        