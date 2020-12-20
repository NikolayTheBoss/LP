# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def SumTreeStack(arg):
    """Функция суммирует значения элементов списка стеком FIFO."""
    tot = 0
    tree = list(arg)
    while tree:
        print(tree)
        print(tot)
        first = tree.pop(0)
        if isinstance(first, list):
            tree.extend(first)
        else:
            tot += first
    return tot


def mysum(arg):
    """Функция суммирует значения элементов списка рекурсией."""
    print(arg)     # Трассировка уровней рекурсии
    L = arg
    if not L:       # На каждом уровне L становится короче
        return 0
    else:
        return L[0] + mysum(L[1:])


def sumtree(sum_list):
    """Функция суммирует все значения включая вложенные списки."""
    tot = 0
    for i in sum_list:
        if isinstance(i, list):
            tot += sumtree(i)
        else:
            tot += i
    return tot


def main(*arg):
    """Основная программа."""
    # a = mysum([1, 2, 5, 6, 100, 74, 15, 5])
    # a = sumtree([1, [2, 3], [1], [2, [15, [7, 8, 13], 11]]])
    a = SumTreeStack([10, [7, [1, 2], 12], [5, 6, 4], 9])
    return a


if __name__ == "__main__":
    print(main())
    print('The End of main programm')
