# BOARDCOVER
# Jaekyoung Kim (rlakim5521@naver.com)

# NOT COMPLETE

class BitMatrix:
    def __init__(self, matrix, row_size, col_size):
        self.matrix = matrix
        self.row_size = row_size
        self.col_size = col_size
    
    # TODO: Test
    def write(self, stream, start_row, start_col):
        self.matrix = self.matrix | ((stream << (start_row * self.col_size)) << start_col)
        return self
    
    # complete
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
    
    # complete
    def rotate(self):
        res = 0
        for iter1 in xrange(self.col_size):
            for iter2 in xrange(self.col_size):
                res = res << 1
                res = res | self.read(1, iter2, self.col_size-iter1-1)
        return BitMatrix(res, self.row_size, self.col_size)
    
    # complete
    def reverseDiagonally(self):
        extractor = 0
        reversedBlock = 0
        for col in xrange(self.col_size):
            extractor = extractor << 1
            extractor = extractor | 1
        for row in xrange(self.row_size):
            originalLine = (self.matrix >> row * self.col_size) & extractor
            for col in xrange(self.col_size):
                reversedBlock = reversedBlock << 1
                reversedBlock = reversedBlock | ((originalLine >> col) & 1)
        return BitMatrix(reversedBlock, self.row_size, self.col_size)
    
    # complete
    def printMatrix(self):
        board = self.matrix
        for printed in xrange(self.row_size*self.col_size-1, -1, -1):
            if((board >> printed) & 1 == 1):
                print '#',
            else:
                print '.',
            if(printed % self.col_size == 0):
                print ""
        print "-----------------------------"
    
    # TODO: When two BitMatrixes have different size, comparing one have to be resized to compared one.
    def is_overlap(self, comparing):
        if(self.row_size == comparing.row_size and self.col_size == comparing.col_size):
            if(self.matrix & comparing.matrix != 0):
                return True
            else:
                return False
    
    # complete
    def overlap(self, overlapping):
        return BitMatrix(self.matrix | overlapping.matrix, self.row_size, self.col_size)

# Main function
if __name__ == "__main__":
    # cache = [[-1 for col in xrange(MAX_INDEX)] for row in xrange(MAX_INDEX)]
    for _ in range(int(raw_input())):
        # Input
        H, W, R, C = map(int, raw_input().split())
        int_board = 0
        for row in xrange(H):
            line = raw_input()
            for col in xrange(W):
                int_board = int_board << 1
                if(line[col] == '#'):
                    int_board = int_board | 1
        int_block = 0
        for row in xrange(H):
            if(row < R):
                line = raw_input()
                for col in xrange(W):
                    int_block = int_block << 1
                    if(col < C):
                        if(line[col] == '#'):
                            int_block = int_block | 1
        int_block = int_block >> (W-C)
        
        # Solve
        board = BitMatrix(int_board, H, W)
        block = BitMatrix(int_block, H, W)
        
        blocks = [
                  block,
                  BitMatrix(block.rotate().matrix >> (W-R), H, W),
                  BitMatrix(block.reverseDiagonally().matrix >> ((H-R)*W) >> (W-C), H, W),
                  BitMatrix(BitMatrix(block.reverseDiagonally().matrix >> ((H-R)*W) >> (W-C), H, W).rotate().matrix >> (W-R), H, W)
                  ]
        
        for blo in blocks:
            blo.printMatrix()
        
        # Output
        print getMaxNumber(board, blocks, 0, R, C)