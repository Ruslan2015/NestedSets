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

    def testtree(self):
        # Ключ (rk, lk, level, id)
        # Читаем файл в словарь
        patternkey = re.compile('\(.*?\)')  # шаблон на все, что между скобок
        patternval = re.compile('".*?"')  # шаблон на все, что между кавычек
        for line in open('files/testtree', 'r'):
            key = patternkey.search(line).group()  # получаем все, что между скобок
            val = patternval.search(line).group()  # получаем все, что между кавычек
            patterndig = re.compile('\d+,*')  # шаблон на числа с запятой сзади и без нее
            dig = patterndig.findall(key[1:-1])  # получаем все числа в строке
            rk = int(dig[0][:-1])  # получаем левый ключ, удаляя запятую
            lk = int(dig[1][:-1])  # получаем правый ключ, удаляя запятую
            lev = int(dig[2][:-1])  # получаем уровень, удаляя запятую
            nid = int(dig[3])  # получаем id (удалять запятую не надо - ее нет)
            self.tree[(rk, lk, lev, nid)] = val[1:-1]

    def showtreetofile(self):
        for node in sorted(self.tree.keys()):
            print(node[2] * '.', node, ' - ', self.tree[node])


if __name__ == "__main__":
    ns = NestedSets()
    ns.testtree()
    ns.showtreetofile()
