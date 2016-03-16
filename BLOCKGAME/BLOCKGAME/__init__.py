# BLOCKGAME
# Jaekyoung Kim (rlakim5521@naver.com)

global cache
global blocks
MAX_INDEX = 33554432

class BitMatrix:
    def __init__(self, matrix, row_size, col_size):
        self.matrix = matrix
        self.row_size = row_size
        self.col_size = col_size
        
    # TODO: When two BitMatrixes have different size, comparing one have to be resized to compared one.
    def is_overlap(self, comparing):
        if(self.matrix & comparing.matrix != 0):
            return True
        else:
            return False
    
    # complete
    def overlap(self, overlapping):
        return BitMatrix(self.matrix | overlapping.matrix, self.row_size, self.col_size)

def play(bm_board):
    ret = cache[bm_board.matrix]
    if(ret != -1):
        return ret
    ret = 0
    for block in blocks:
        if(not bm_board.is_overlap(block)):
            if(play(bm_board.overlap(block))==0):
                ret = 1;
                break;
    cache[bm_board.matrix] = ret
    return ret

# Main function
if __name__ == "__main__":
    blocks = []
    
    #   . .
    #   # #
    for row in xrange(5):
        for col in xrange(4):
            blocks.append(BitMatrix(3 << (row * 5 + col),5,5))
    
    
    #   . #
    #   . #
    for row in xrange(4):
        for col in xrange(5):
            blocks.append(BitMatrix(33 << (row * 5 + col),5,5))
    
    #   # .
    #   # #
    for row in xrange(4):
        for col in xrange(4):
            blocks.append(BitMatrix(67 << (row * 5 + col),5,5))
    
    
    #   . #
    #   # #
    for row in xrange(4):
        for col in xrange(4):
            blocks.append(BitMatrix(35 << (row * 5 + col),5,5))
    
    #   # #
    #   . #
    for row in xrange(4):
        for col in xrange(4):
            blocks.append(BitMatrix(97 << (row * 5 + col),5,5))
    
    #   # #
    #   # .
    for row in xrange(4):
        for col in xrange(4):
            blocks.append(BitMatrix(98 << (row * 5 + col),5,5))
    
    cache = [-1 for _ in xrange(MAX_INDEX)]
    
    for _ in range(int(raw_input())):
        
        # Input
        int_board = 0
        for row in xrange(5):
            line = raw_input()
            for col in xrange(5):
                int_board = int_board << 1
                if(line[col] == '#'):
                    int_board = int_board | 1
        
        bm_board = BitMatrix(int_board, 5, 5)
        
        # Output
        if(play(bm_board)==1):
            print "WINNING"
        else:
            print "LOSING"