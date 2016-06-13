# EDITORWARS
# Jaekyoung Kim (rlakim5521@naver.com)

import sys
from cookielib import reach
input = sys.stdin.readline

class Union_Find:
    def __init__(self, N):
        self.N = N
        self.ACKtree = [iter for iter in xrange(N)]
        self.DISlist = [-1] * N
        
    def getRoot(self, child):
        current = child
        parent = self.ACKtree[current]
        while current != parent:
            current = parent
            parent = self.ACKtree[current]
        return parent
            
        
    def insert(self, attitude, user_1, user_2):
        if attitude == "ACK":
            self.ACKtree[self.getRoot(user_2)] = self.getRoot(user_1)
        else:
            if self.DISlist[self.getRoot(user_1)] != -1:
                
        

def solve(N, M, UF):
    for info_iter in xrange(M):
        information = input().split()
        attitude = information[0]
        user_1 = int(information[1])
        user_2 = int(information[2])
    
# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        # Input
        N, M = map(int, input().split())
        UF = Union_Find(N)
        
        # Solve
        solve(N, M, UF)