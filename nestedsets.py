# -*-  coding: utf-8 -*-
import re


class NestedSets:
    def __init__(self):
        self.id = 0
        self.level = 0
        self.rk = 0
        self.lk = 0
        self.ref = ''
        self.tree = {}

    def readtesttree(self):
        # Ключ в словарь записывается так - (rk, lk, level, id)
        # Читаем файл в словарь
        patternkey = re.compile('\(.*?\)')  # шаблон на все, что между скобок
        patternval = re.compile('".*?"')  # шаблон на все, что между кавычек
        for line in open('files/testtree', 'r'):
            key = patternkey.search(line).group()  # получаем все, что между скобок
            val = patternval.search(line).group()  # получаем все, что между кавычек
            patterndig = re.compile('\d+,*')  # шаблон на числа с запятой сзади и без нее
            dig = patterndig.findall(key[1:-1])  # получаем все числа в строке
            # получаем левый ключ, удаляя запятую, получаем правый ключ, удаляя запятую,
            # получаем уровень, удаляя запятую, получаем id (удалять запятую не надо - ее нет)
            self.tree[int(dig[0][:-1]), int(dig[1][:-1]), int(dig[2][:-1]), int(dig[3])] = val[1:-1]

    def displaytreetofile(self):
        fd = open('files/displaytree', 'w')
        item = """
          +---+
          |   |
        +---+---+
        |   |   |
        +---+---+
        |   |   |
        +---+---+
        """
        for node in sorted(self.tree.keys()):
            fstr = node[2] * '.' + str(node) + ' - ' + self.tree[node] + '\n'
            fd.write(fstr)
        fd.write(item)
        fd.close()


if __name__ == "__main__":
    ns = NestedSets()
    ns.readtesttree()
    ns.displaytreetofile()
