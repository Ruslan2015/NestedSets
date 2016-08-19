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
        # Ключ в словарь записывается так - (rk, lk, level, id)
        # 0        |
        # 1    +-------+
        # 2    |  inf  |
        # 3    +---+---+
        # 4    | id|lev|
        # 5    +---+---+
        # 6    | lk| rk|
        # 7    +---+---+
        # отдельный узел
        nodeitem = ["    |    ",
                    "+-------+",
                    "|       |",
                    "+---+---+",
                    "|   |   |",
                    "+---+---+",
                    "|   |   |",
                    "+---+---+"]
        width = 9  # ширина узла
        distance = 3  # расстояние между узлами

        # тестово отобразим узлы ввсех уровней без учета вложенности
        # 1 - узнаем максимальное значение уровня в ключах
        max_lev = 0
        for key in self.tree.keys():
            if key[2] > max_lev:
                max_lev = key[2]
        # создаем список-страницу
        page_nodes = []
        for lev_nodes in range(max_lev):
            page_nodes.append(lev_nodes)
        # заполняем каждый уровень
        levellines = {}  # наборы строк для каждого уровня
        for (current_level, level) in enumerate(page_nodes):
            nodelines = []  # набор строк уровня
            for (count_item_line, itemline) in enumerate(nodeitem):
                nodeline = ""  # строка в уровне
                for key in sorted(self.tree.keys()):
                    if key[2] == current_level + 1:
                        # здесь должны вставляться цифры
                        if count_item_line == 4:
                            itemline = '|{0!s:>3}|{1!s:>3}|'.format(key[3], key[2])
                        if count_item_line == 6:
                            itemline = '|{0!s:>3}|{1!s:>3}|'.format(key[0], key[1])
                        # TODO: Сюда необходимо вставить рассчет интервалов по алгоритму
                        # 1 - получить всю ветку от родителя и ниже
                        # 2 - взять максимальный уровень и к-во элементов в нем и умножить на width
                        nodeline = nodeline + " " * distance + itemline
                nodelines.append("    " * current_level + nodeline + "\n")
            levellines[level] = nodelines

        for key in levellines.keys():
            for lin in levellines[key]:
                fd.write(lin)

        fd.close()

    def add_node(self, parent):
        # Обновляем ключи узлов, стоящих за родительским узлом
        # UPDATE my_tree SET left_key = left_key + 2, right_ key = right_ key + 2 WHERE left_key > $right_ key
        # Обновляем родительскую ветку
        # UPDATE my_tree SET right_key = right_key + 2 WHERE right_key >= $right_key AND left_key < $right_key
        # Добавляемновый узел
        # INSERT INTO my_tree SET left_key = $right_key, right_key = $right_key + 1, level = $level + 1
        pass

    def del_node(self, nid):
        pass

    def test_tree(self):
        pass


if __name__ == "__main__":
    ns = NestedSets()
    ns.readtesttree()
    ns.displaytreetofile()
