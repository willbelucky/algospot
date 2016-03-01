# BOARDCOVER2
# Jaekyoung Kim (rlakim5521@naver.com)

def printBoard(board, H, W):
    for printed in xrange(H*W-1, -1, -1):
        if(board >> printed & 1 == 1):
            print '#',
        else:
            print '.',
        if(printed % W == 0):
            print ""

# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        # Input
        H, W, R, C = map(int, raw_input().split())
        board = 0
        for row in xrange(H):
            line = raw_input()
            for col in xrange(W):
                board = board << 1
                if(line[col] == '#'):
                    board = board | 1
        block = 0
        for row in xrange(H):
            if(row < R):
                line = raw_input()
                for col in xrange(W):
                    block = block << 1
                    if(col < C):
                        if(line[col] == '#'):
                            block = block | 1
        
        print board
        print block >> 1
        print block << 2 * W
        printBoard(block >> 1, H, W)
        printBoard(block << 2 * W, H, W)