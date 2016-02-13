# GENIUS
# Jaekyoung Kim (rlakim5521@naver.com)

from math import ceil, log

# Products matrix A and matrix B which are n*n matrixes
def ikjMatrixProduct(A, B, n):
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for k in xrange(n):
            for j in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def add(A, B, n):
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtract(A, B, n):
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def strassenR(A, B, n):
    """ 
        Implementation of the strassen algorithm.
    """

    if n <= 2:
        return ikjMatrixProduct(A, B, n)
    else:
        # initializing the new sub-matrices
        newSize = n/2
        a11 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        a12 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        a21 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        a22 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]

        b11 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        b12 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        b21 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        b22 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]

        aResult = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        bResult = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]

        # dividing the matrices in 4 sub-matrices:
        for i in xrange(0, newSize):
            for j in xrange(0, newSize):
                a11[i][j] = A[i][j]            # top left
                a12[i][j] = A[i][j + newSize]    # top right
                a21[i][j] = A[i + newSize][j]    # bottom left
                a22[i][j] = A[i + newSize][j + newSize] # bottom right
 
                b11[i][j] = B[i][j]            # top left
                b12[i][j] = B[i][j + newSize]    # top right
                b21[i][j] = B[i + newSize][j]    # bottom left
                b22[i][j] = B[i + newSize][j + newSize] # bottom right

        # Calculating p1 to p7:
        aResult = add(a11, a22, newSize)
        bResult = add(b11, b22, newSize)
        p1 = strassenR(aResult, bResult, newSize) # p1 = (a11+a22) * (b11+b22)
 
        aResult = add(a21, a22, newSize)      # a21 + a22
        p2 = strassenR(aResult, b11, newSize)  # p2 = (a21+a22) * (b11)
 
        bResult = subtract(b12, b22, newSize) # b12 - b22
        p3 = strassenR(a11, bResult, newSize)  # p3 = (a11) * (b12 - b22)
 
        bResult = subtract(b21, b11, newSize) # b21 - b11
        p4 =strassenR(a22, bResult, newSize)   # p4 = (a22) * (b21 - b11)
 
        aResult = add(a11, a12, newSize)      # a11 + a12
        p5 = strassenR(aResult, b22, newSize)  # p5 = (a11+a12) * (b22)   
 
        aResult = subtract(a21, a11, newSize) # a21 - a11
        bResult = add(b11, b12, newSize)      # b11 + b12
        p6 = strassenR(aResult, bResult, newSize) # p6 = (a21-a11) * (b11+b12)
 
        aResult = subtract(a12, a22, newSize) # a12 - a22
        bResult = add(b21, b22, newSize)      # b21 + b22
        p7 = strassenR(aResult, bResult, newSize) # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        c12 = add(p3, p5, newSize) # c12 = p3 + p5
        c21 = add(p2, p4, newSize)  # c21 = p2 + p4
 
        aResult = add(p1, p4, newSize) # p1 + p4
        bResult = add(aResult, p7, newSize) # p1 + p4 + p7
        c11 = subtract(bResult, p5, newSize) # c11 = p1 + p4 - p5 + p7
 
        aResult = add(p1, p3, newSize) # p1 + p3
        bResult = add(aResult, p6, newSize) # p1 + p3 + p6
        c22 = subtract(bResult, p2, newSize) # c22 = p1 + p3 - p2 + p6
 
        # Grouping the results obtained in a single matrix:
        C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
        for i in xrange(0, newSize):
            for j in xrange(0, newSize):
                C[i][j] = c11[i][j]
                C[i][j + newSize] = c12[i][j]
                C[i + newSize][j] = c21[i][j]
                C[i + newSize][j + newSize] = c22[i][j]
        return C

def strassen(A, B, n):

    # Make the matrices bigger so that you can apply the strassen
    # algorithm recursively without having to deal with odd
    # matrix sizes
    nextPowerOfTwo = lambda n: 2**int(ceil(log(n,2)))
    m = nextPowerOfTwo(n)
    APrep = [[0 for i in xrange(m)] for j in xrange(m)]
    BPrep = [[0 for i in xrange(m)] for j in xrange(m)]
    for i in xrange(n):
        for j in xrange(n):
            APrep[i][j] = A[i][j]
            BPrep[i][j] = B[i][j]
    CPrep = strassenR(APrep, BPrep, n)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            C[i][j] = CPrep[i][j]
    return C

# Involves n*n matrix by Strassen algorithm with divide and conquer method.
def powByStrassen(matrix, k, n):
    if(k == 1):
        return matrix
    elif(k == 2):
        return strassen(matrix, matrix, n)
    else:
        return strassen(powByStrassen(matrix, k/2, n), powByStrassen(matrix, k-k/2, n), n)

# Involves n*n matrix by ijk-product algorithm with divide and conquer method.
def powByIjk(matrix, k, n):
    if(k == 1):
        return matrix
    elif(k == 2):
        return ikjMatrixProduct(matrix, matrix, n)
    else:
        return ikjMatrixProduct(powByIjk(matrix, k/2, n), powByIjk(matrix, k-k/2, n), n)

def printMatrix(matrix):
    for line in matrix:
        print "\t".join(map(str,line))
        
# Main function
if __name__ == "__main__":
    for _ in xrange(int(raw_input())):
        # Input
        n, k, m = map(int, raw_input().split())
        len = [0] * n
        len = map(int, raw_input().split())
        T = [[0.0] * n for _ in xrange(n)]
        for _ in xrange(n):
            T[_] = map(float, raw_input().split())
        favorites = [0] * n
        favorites = map(int, raw_input().split())
        
        # Solve
        powOfTow = [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288]
        count = powOfTow.count(n)
        if(count == 1):
            W = [[0.0] * (4*n) for _ in xrange(4*n)]
            for i in xrange(3*n):
                W[i][i+n] = 1.0
            for i in xrange(n):
                for j in xrange(n):
                    W[3*n+i][(4-len[j])*n+j] = T[j][i]
            Wk = powByStrassen(W, k, 4*n)
        else:
            W = [[0.0] * (4*n) for _ in xrange(4*n)]
            for i in xrange(3*n):
                W[i][i+n] = 1.0
            for i in xrange(n):
                for j in xrange(n):
                    W[3*n+i][(4-len[j])*n+j] = T[j][i]
            Wk = powByIjk(W, k, 4*n)
        
        # Output
        for favorite in favorites:
            result = 0.0
            for start in xrange(len[favorite]):
                result += Wk[(3-start)*n+favorite][3*n]
            print result,
        print