# -*- coding: utf-8 -*-
"""
Задания к Части 3
Created on Wed Dec 16 13:41:44 2020

@author: user
"""


def task_4():
    L = []
    for i in range(10):
        L.append(2**i)
    X = 7
    if 2**X in L:
        print('at index', L.index(2**X))
    else:
        print(X, 'not found')


def main():
    task_4()


if __name__ == '__main__':
    main()
