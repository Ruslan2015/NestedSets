# -*-  coding: utf-8 -*-


class NestedSets:
    def __init__(self):
        self.id = 0
        self.level = 0
        self.rk = 0
        self.lk = 0
        self.ref = ''
        self.tree = []

    def getfrombase(self):
        self.tree = {"1,1,1,2": "ref1"}

    def showtreetofile(self):
        for node in self.tree:
            print(node.key)

if __name__ == "__main__":
    ns = NestedSets()
    ns.showtreetofile()
