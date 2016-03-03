'''
Created on 2016. 3. 3.

@author: jk
'''

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