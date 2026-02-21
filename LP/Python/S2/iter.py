class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def addChild(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ithChild(self, i):
        return self.child[i]
       
    def num_children(self):
        res = len(self.child)
        for i in self.child:
            res += i.num_children()
        return res
    def __iter__(self):
        res = self.rt
        yield res
        stack = self.child
        while stack:
            n = stack.pop(0)
            yield n.rt
            stack += n.child
    
