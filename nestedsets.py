# -*-  coding: utf-8 -*-


class NestedSets:
    def __init__(self):
        self.id = 0
        self.level = 0
        self.rk = 0
        self.lk = 0
        self.ref = ''
        self.tree = []

    @staticmethod
    def showtreetofile():
        print("Тест")
        print("Вторая строчка")

if __name__ == "__main__":
    ns = NestedSets()
    ns.showtreetofile()
