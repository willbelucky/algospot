# PICNIC
# Jaekyoung Kim (rlakim5521@naver.com)

# Gets the number of pairing
# A start is a first number of iterator for preventing overlapping counting.
# A status is a bit-mask which expresses each student whether has a partner.
# A goal is a bit-mask with 1 of n. When status is equal to goal, the function
# return 1.
# A friendshipMatrix expresses whether two students are friend or not.
def getNumberOfPairing(start, status, goal, friendshipMatrix):
    if(status == goal):
        return 1
    
    ret = 0
    
    for i in xrange(start, n):
        for j in xrange(i+1,n):
            if(status&(1<<i)==0 and status&(1<<j)==0 and friendshipMatrix[i][j]==1):
                ret += getNumberOfPairing(i+1, status|(1<<i)|(1<<j), goal, friendshipMatrix)
    
    return ret

# Main function
if __name__ == "__main__":
    for _ in xrange(int(raw_input())):
        # Input
        n, m = map(int, raw_input().split())
        friendshipList = map(int, raw_input().split())
        friendshipMatrix = [[0] * n for _ in xrange(n)]
        for iter in xrange(m):
            friendshipMatrix[friendshipList[2*iter]][friendshipList[2*iter+1]]=1
            friendshipMatrix[friendshipList[2*iter+1]][friendshipList[2*iter]]=1
        status = 0
        goal = 0
        for iter in xrange(n):
            goal = goal << 1
            goal = goal | 1
        
        print getNumberOfPairing(0, status, goal, friendshipMatrix)