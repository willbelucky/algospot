# BLOCKGAME
# Jaekyoung Kim (rlakim5521@naver.com)

global cache
global blocks
MAX_INDEX = 33554432

def play(int_board):
    ret = cache[int_board]
    if(ret != -1):
        return ret
    ret = 0
    for block in blocks:
        if(int_board & block == 0):
            if(play(int_board | block) == 0):
                ret = 1;
                break;
    cache[int_board] = ret
    return ret

# Main function
if __name__ == "__main__":
    cache = [-1 for _ in xrange(MAX_INDEX)]
    
    blocks = []
    
    #   . .
    #   # #
    for row in xrange(5):
        for col in xrange(4):
            blocks.append(3 << (row * 5 + col))
    
    
    #   . #
    #   . #
    for row in xrange(4):
        for col in xrange(5):
            blocks.append(33 << (row * 5 + col))
    
    #   # .
    #   # #
    for row in xrange(4):
        for col in xrange(4):
            blocks.append(67 << (row * 5 + col))
    
    
    #   . #
    #   # #
    for row in xrange(4):
        for col in xrange(4):
            blocks.append(35 << (row * 5 + col))
    
    #   # #
    #   . #
    for row in xrange(4):
        for col in xrange(4):
            blocks.append(97 << (row * 5 + col))
    
    #   # #
    #   # .
    for row in xrange(4):
        for col in xrange(4):
            blocks.append(98 << (row * 5 + col))
    
    for _ in range(int(raw_input())):
        
        # Input
        int_board = 0
        for row in xrange(5):
            line = raw_input()
            for col in xrange(5):
                int_board = int_board << 1
                if(line[col] == '#'):
                    int_board = int_board | 1
        
        # Output
        if(play(int_board)==1):
            print "WINNING"
        else:
            print "LOSING"