# QUANTIZE
# Jaekyoung Kim (rlakim5521@naver.com)

global n
global s
global pSum
global pSqSum
global cache

def preCalc():
    
    pSum[0] = numbers[0]
    pSqSum[0] = numbers[0] * numbers[0]
    for _ in xrange(1, n):
        pSum[_] = pSum[_-1] + numbers[_]
        pSqSum[_] = pSqSum[_-1] + numbers[_] * numbers[_]

def minError(lo, hi):
    if(lo==0):
        sum = pSum[hi]
        sqSum = pSqSum[hi]
        m = int(0.5 + float(sum) / (hi - lo + 1))
        ret = sqSum - 2 * m * sum + m * m * (hi - lo + 1)
        return ret
    else:
        sum = pSum[hi] - pSum[lo-1]
        sqSum = pSqSum[hi] - pSqSum[lo-1]
        m = int(0.5 + float(sum) / (hi - lo + 1))
        ret = sqSum - 2 * m * sum + m * m * (hi - lo + 1)
        return ret


def quantize(start, parts):
    
    if(start == n):
        return 0
    if(parts == 1): return minError(start, n - 1)
    ret = cache[start][parts]
    if(ret != 1000000): return ret
    for partSize in xrange(1, n - start + 1):
        ret = min(ret, minError(start, start + partSize - 1) + quantize(start + partSize, parts - 1))
        
    cache[start][parts] = ret
    return ret
    

# Main function
if __name__ == "__main__":
    for _ in xrange(int(raw_input())):
        n, s = map(int, raw_input().split())
        numbers = map(int, raw_input().split())
        numbers.sort()
        pSum = [0] * n
        pSqSum = [0] * n
        cache = [[1000000] * (s+1) for _ in xrange(n)]
        preCalc()
        print quantize(0, s)