class FiboIterator:
    def __init__(self,FE,SE,N):
        self.FE = FE
        self.SE = SE
        self.N = N
    def __iter__(self):
        self.i=1
        return self
    def __next__(self):
        if self.i <= self.N:
            res = self.FE
            self.FE = self.SE
            self.SE = self.SE+res
            self.i = self.i+1
            return res
        raise StopIteration
FS=FiboIterator(2,3,10)
for i in FS:
    print(i)
