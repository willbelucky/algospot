# BOARDCOVER2
# Jaekyoung Kim (rlakim5521@naver.com)

global cache

MAX_INDEX = 536870912

class BitMatrix:
    def __init__(self, matrix, row_size, col_size):
        self.matrix = matrix
        self.row_size = row_size
        self.col_size = col_size
    
    # TODO: Test
    def write(self, stream, start_row, start_col):
        self.matrix = self.matrix | ((stream << (start_row * self.col_size)) << start_col)
        return self
    
    # TODO: Test
    def read(self, length, start_row, start_col):
        extractor = 0
        for iter in xrange(length):
            extractor = (extractor << 1) | 1
       
        readStream = (self.matrix >> (self.col_size * start_row) >> start_col) & extractor
        return readStream
    
    # complete
    def compare(self, comparing):
        if(self.row_size == comparing.row_size 
           and self.col_size == comparing.col_size 
           and self.matrix == comparing.matrix):
            return True
        else:
            return False
        
    # TODO: We need write and read function.
    def resize(self, new_row_size, new_col_size):
        resizedMatrix = BitMatrix(0, new_row_size, new_col_size)
        
    # TODO: When two BitMatrixes have different size, comparing one have to be resized to compared one.
    def is_overlap(self, comparing):
        if(self.row_size == comparing.row_size and self.col_size == comparing.col_size):
            if(self.matrix & comparing.matrix != 0):
                return True
            else:
                return False
    

class Block:
    def __init__(self, block, R, C):
        self.block = block
        self.R = R
        self.C = C

def reverseDiagonally(block, H, W, R, C):
    extractor = 0
    reversedBlock = 0
    for col in xrange(W):
        extractor = extractor << 1
        extractor = extractor | 1
    for row in xrange(H):
        originalLine = (block >> row * W) & extractor
        for col in xrange(W):
            reversedBlock = reversedBlock << 1
            reversedBlock = reversedBlock | ((originalLine >> col) & 1)
    reversedBlock = (reversedBlock >> ((H-R)*W)) >> (W-C)
    return reversedBlock

def rotate(block, H, W, R, C):
    reversedBlock = 1
    for row in xrange(C):
        for col in xrange(R):
            reversedBlock = reversedBlock << 1
            reversedBlock = reversedBlock | 1
            printBoard(reversedBlock, H, W)
        reversedBlock = reversedBlock << (W - R + 1)
    return reversedBlock
            
def getMax(board, blocks, h, w, H, W):
    if(board < MAX_INDEX):
        if(cache[board] != -1):
            return cache[board]
    
    retList = [0]
    for num in xrange(4):
        print num, H-blocks[num].R, W-blocks[num].C
        for row in xrange(H-blocks[num].R+1):
            for col in xrange(W-blocks[num].C+1):
                if(num == 2 and row == 2 and col == 0):
                    print "========================================"
                    printBoard(board & ((blocks[num].block << (row*W)) << col), H, W)
                    print "========================================"
                if(board & ((blocks[num].block << (row*W)) << col) == 0):
                    retList.append(getMax(board | (blocks[num].block << (row*W) << col), blocks, row, col, H, W)+1)
                
    if not retList:
        printBoard(board, H, W)
        print "-------------------------------------------------"
        
    if h == 0 and w == 0:
        print retList
    maxVal = max(retList)
    if(board < MAX_INDEX):
        cache[board] = maxVal
    return maxVal

def printBoard(board, H, W):
    for printed in xrange(H*W-1, -1, -1):
        if((board >> printed) & 1 == 1):
            print '#',
        else:
            print '.',
        if(printed % W == 0):
            print ""
    print "-----------------------------"

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
        block = block >> (W-C)
        
                       
        blocks = [
                  Block(block, R, C),
                  Block(reverseDiagonally(block, H, W, R, C), R, C),
                  Block(rotate(block, H, W, R, C), C, R),
                  Block(rotate(reverseDiagonally(block, H, W, R, C), H, W, R, C), C, R)
                  ]
        
        for iter in xrange(4):
            printBoard(blocks[iter].block, H, W)
        
        """
        for iter in xrange(4):
            print blocks[iter].R, blocks[iter].C
         """
            
        # Solve
        cache = [-1] * MAX_INDEX
        ret = getMax(board, blocks, 0, 0, H, W)
        
        # Output
        print ret