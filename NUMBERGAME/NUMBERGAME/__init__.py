# NUMBERGAME
# Jaekyoung Kim (rlakim5521@naver.com)

MinValue = -987654321

def getOptical(left, right, cache, gBoard):
    
    if(left > right): return 0
    ret = cache[left][right]
    if(ret != MinValue): return ret
    ret = max(gBoard[left]-getOptical(left+1, right, cache, gBoard),
              gBoard[right]-getOptical(left, right-1, cache, gBoard))
    if(right > left):
        ret = max(ret,
                  0-getOptical(left+2, right, cache, gBoard),
                  0-getOptical(left, right-2, cache, gBoard)
                  )
    cache[left][right] = ret
    return ret


# Main function
if __name__ == "__main__":
    for _ in xrange(int(raw_input())):
        # Input
        len = int(raw_input())
        gBoard = map(int,raw_input().split())
        cache = [[MinValue]*len for _ in xrange(len)]
        # Output
        print getOptical(0, len - 1, cache, gBoard)