class UnionFind(object):
    # quick weighted union find
    
    def __init__(self, nums):
        self.data = nums
        self.parents = [a for a in xrange(len(nums))]
        self.size = [1] * len(nums)
        self.count = len(nums)
        
    def find(self, index):
        while self.parents[index] != index:
            index = self.parents[index]
        return index
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return
        if self.size[rootP] < self.size[rootQ]:
            
            self.parents[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parents[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        self.count -= 1
        
    def connected(self, p , q):
        return self.find(p) == self.find(q)
    
    def max_size(self):
        if not self.size:
            return 0
        return max(self.size)
            
        
