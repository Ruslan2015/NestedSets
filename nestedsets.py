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
        # дописав код ниже про интервалы получим не тестовое отображение
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
                            itemline = '|{0!s:>3}|{1!s:>3}|'.format(key[1], key[0])
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
<<<<<<< HEAD
 
    def add_node(self, parent):
        # parent = (rk, lk, level, id)
        # Обновляем ключи узлов, стоящих за родительским узлом
        # UPDATE my_tree SET left_key = left_key + 2, right_ key = right_ key + 2 WHERE left_key > $right_ key
        # создаем временную копию дерева, т.к. при перепысывании ключей они повторно
        # могут попасть в цикл
        tmp_tree = self.tree
        # обходим основное дерево, и там где необходимо поменять ключи, меняем их в
        # копии дерева
        for key in self.tree.keys():
            if key[1] > parent[0]:
                # сохраняем ключ и значение во временных переменных
                tmp_key = key
                tmp_val = self.tree[key]
                # удалаем элемент с текущим ключем из обоих деревьев
                pass
                # рассчитываем новые ключи
                tmp_key[1] = tmp_key[1] + 2
                tmp_key[0] = tmp_key[0] + 2
                # воссоздаем узел с обновленными ключами в копии дерева
                tmp_tree[tmp_key] = tmp_val
        # обновляем основное дерево
        self.tree = tmp_tree
        
        # Обновляем родительскую ветку
        # UPDATE my_tree SET right_key = right_key + 2 WHERE right_key >= $right_key AND left_key < $right_key
        # Добавляемновый узел
=======

    def add_node(self, parent, val):
        # parent = (rk, lk, level, id)
        # обходим основное дерево, делаем его копию, и там где необходимо поменять ключи, меняем их в копии
        copy_tree = {}
        next_id = 0
        for key in self.tree.keys():
            # сохраняем ключ и значение во временных переменных
            tmp_rk = key[0]
            tmp_lk = key[1]
            tmp_lev = key[2]
            tmp_id = key[3]
            tmp_val = self.tree[key]
            # Обновляем ключи узлов, стоящих за родительским узлом
            # UPDATE my_tree SET left_key = left_key + 2, right_ key = right_ key + 2 WHERE left_key > $right_ key
            if key[1] > parent[0]:
                # рассчитываем новые ключи
                tmp_lk += 2
                tmp_rk += 2
                new_key = (tmp_rk, tmp_lk, tmp_lev, tmp_id)
                # воссоздаем узел с обновленными ключами в копии дерева
                copy_tree[new_key] = tmp_val
            # Обновляем родительскую ветку
            # UPDATE my_tree SET right_key = right_key + 2 WHERE right_key >= $right_key AND left_key < $right_key
            elif key[0] >= parent[0] > key[1]:
                tmp_rk += 2
                new_key = (tmp_rk, tmp_lk, tmp_lev, tmp_id)
                copy_tree[new_key] = tmp_val
            else:
                # просто создаем копию записи
                copy_tree[(tmp_rk, tmp_lk, tmp_lev, tmp_id)] = tmp_val
            # вычисляем максимальный id для создания нового
            if key[3] >= next_id:
                next_id = key[3] + 1
        # Добавляем новый узел
>>>>>>> 3d331f47d53fdf767abd8847ffbc3a4c5caeb5c8
        # INSERT INTO my_tree SET left_key = $right_key, right_key = $right_key + 1, level = $level + 1
        add_lk = parent[0]
        add_rk = parent[0] + 1
        add_lev = parent[2] + 1
        key = (add_rk, add_lk, add_lev, next_id)
        copy_tree[key] = val
        # TODO: выполнить проверку на целостность дерева
        # воссоздаем основное дерево
        self.tree = copy_tree.copy()

        # выводим для отладки на экран
        for key in self.tree.keys():
            print(key, '-', self.tree[key])
        # TODO: сделять резервную копию файла и записать новый файл

    def del_node(self, nid):
        pass

    def test_tree(self):
        # Проверка целостности дерева
        # 1. Левый ключ ВСЕГДА меньше правого;
        error_1 = []  # список с ошибками
        # 2. Наименьший левый ключ ВСЕГДА равен 1;
        # 3. Наибольший правый ключ ВСЕГДА равен двойному числу узлов;
        # 4. Разница между правым и левым ключом ВСЕГДА нечетное число;
        error_2 = []
        # 5. Если уровень узла нечетное число то тогда левый ключ ВСЕГДА нечетное число, то же самое и для четных чисел;
        error_3 = []
        # 6. Ключи ВСЕГДА уникальны, вне зависимости от того правый он или левый;
        min_lk = 2
        max_rk = 0
        for (num_item, key) in enumerate(self.tree.keys()):
            # 1. Левый ключ ВСЕГДА меньше правого;
            if key[1] >= key[0]:
                error_1.append(key[3] + ' - ' + self.tree[key])
            # вычисляем наименьший левый и наибольший правый ключи
            if key[1] < min_lk:
                min_lk = key[1]
            if key[0] > max_rk:
                max_rk = key[0]
            # 4. Разница между правым и левым ключом ВСЕГДА нечетное число;
            if (key[0] - key[1]) % 2 == 0:
                error_2.append(key[3] + ' - ' + self.tree[key])
            # 5. Если уровень узла нечетное число то тогда левый ключ ВСЕГДА нечетное число,
            if (key[2] % 2 != 0) and (key[1] % 2 == 0):
                error_3.append(key[3] + ' - ' + 'узел и ключ ошибка на нечетность')
            # то же самое и для четных чисел;
            if (key[2] % 2 == 0) and (key[1] % 2 != 0):
                error_3.append(key[3] + ' - ' + 'узел и ключ ошибка на четность')
            # TODO: дописать проверку на уникальность
        # TODO: дописать проверку п. 2 и п. 3 с использованием min_lk и max_rk, а также пустоты списков error

if __name__ == "__main__":
    ns = NestedSets()
    ns.readtesttree()
    ns.displaytreetofile()
    key_parent = (5, 2, 2, 2)
    ns.add_node(key_parent, 'node005')
    print('---------------------------------------')
    key_parent = (9, 8, 2, 3)
    ns.add_node(key_parent, 'node006')
    ns.test_tree()
