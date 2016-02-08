# PI
# Jaekyoung Kim (rlakim5521@naver.com)

def getPI(result, PI, length):
    result[3] = getDifficulty(PI[0:3], 3)
    result[4] = getDifficulty(PI[0:4], 4)
    result[5] = getDifficulty(PI[0:5], 5)
    for _ in xrange(6, length + 1):
        result[_] = min(result[_ - 3] + getDifficulty(PI[_ - 3:_], 3),
                        result[_ - 4] + getDifficulty(PI[_ - 4:_], 4),
                        result[_ - 5] + getDifficulty(PI[_ - 5:_], 5))

def getDifficulty(partialPI, length):
    partialIntPI = [0] * length
    for _ in xrange(length):
        partialIntPI[_] = int(partialPI[_])
        
    if partialIntPI[0] == partialIntPI[1]:
        if partialPI == partialPI[0] * length:
            return 1
        else:
            return 10
    
    if partialIntPI[0] - partialIntPI[1] == partialIntPI[1] - partialIntPI[2]:
        for _ in xrange(1, length - 2):
            if partialIntPI[_] - partialIntPI[_ + 1] != partialIntPI[_ + 1] - partialIntPI[_ + 2]:
                return 10
        if abs(partialIntPI[0] - partialIntPI[1]) == 1:
            return 2
        else:
            return 5
    
    for _ in xrange(2, length):
        if(partialIntPI[_] != partialIntPI[_ % 2]):
            return 10
    
    return 4

# Create a result for memoization
result = [0] * 10001
result[0] = result[1] = result[2] = 100000

# Main function
if __name__ == "__main__":
    
    for _ in xrange(int(raw_input())):
        # Input
        PI = raw_input()
        length = len(PI)
        
        # Gets a result of difficulty
        getPI(result, PI, length)
        
        # Output
        print (result[length])