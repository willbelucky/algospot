# MORDOR
# Jaekyoung Kim (rlakim5521@naver.com)

import gc

INT_MAX = 20001
INT_MIN = -1

class minRMQ:
    def __init__(self, array):
        self.n = len(array)
        self.rangeMin = [0] * (4*self.n)
        self._init(array, 0, self.n-1, 1)
        gc.collect()
        
    def _init(self, array, left, right, node):
        if(left == right):
            self.rangeMin[node] = array[left]
            return self.rangeMin[node]
        mid = (left + right) / 2
        leftMin = self._init(array, left, mid, node * 2)
        rightMin = self._init(array, mid + 1, right, node * 2 + 1)
        self.rangeMin[node] = min(leftMin, rightMin)
        return self.rangeMin[node]
    
    def query(self, left, right):
        return self._query(left, right, 1, 0, self.n-1)
    
    def _query(self, left, right, node, nodeLeft, nodeRight):
        if(right < nodeLeft or nodeRight < left):
            return INT_MAX
        if(left <= nodeLeft and nodeRight <= right):
            return self.rangeMin[node]
        mid = (nodeLeft + nodeRight) / 2
        return min(self._query(left, right, node*2, nodeLeft, mid), self._query(left, right, node*2+1, mid+1, nodeRight))

class maxRMQ:
    def __init__(self, array):
        self.n = len(array)
        self.rangeMax = [0] * (4*self.n)
        self._init(array, 0, self.n-1, 1)
        gc.collect()
        
    def _init(self, array, left, right, node):
        if(left == right):
            self.rangeMax[node] = array[left]
            return self.rangeMax[node]
        mid = (left + right) / 2
        leftMax = self._init(array, left, mid, node * 2)
        rightMax = self._init(array, mid + 1, right, node * 2 + 1)
        self.rangeMax[node] = max(leftMax, rightMax)
        return self.rangeMax[node]
    
    def query(self, left, right):
        return self._query(left, right, 1, 0, self.n-1)
    
    def _query(self, left, right, node, nodeLeft, nodeRight):
        if(right < nodeLeft or nodeRight < left):
            return INT_MIN
        if(left <= nodeLeft and nodeRight <= right):
            return self.rangeMax[node]
        mid = (nodeLeft + nodeRight) / 2
        return max(self._query(left, right, node*2, nodeLeft, mid), self._query(left, right, node*2+1, mid+1, nodeRight))


# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        # Input
        N, Q = map(int, raw_input().split())
        h = map(int, raw_input().split())
        minimumRMQ = minRMQ(h)
        maximumRMQ = maxRMQ(h)
        for _ in xrange(Q):
            a, b = map(int, raw_input().split())
            print maximumRMQ.query(a, b) - minimumRMQ.query(a, b)