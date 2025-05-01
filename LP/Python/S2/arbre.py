class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ith_child(self, i):
        return self.child[i]
       
    def num_children(self):
        res = len(self.child)
        for i in self.child:
            res += i.num_children()
        return res

class Pre(Tree):
    def preorder(self):
        res = [self.root()]
        for i in self.child:
            res += i.preorder()
        return res 
        