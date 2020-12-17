# -*- coding: utf-8 -*-
"""
Задания к Части 3
Created on Wed Dec 16 13:41:44 2020

@author: user
"""


def task_4():
    L = []
    for i in range(6):
        L.append(2**i)
    X = 5
    found = False
    i = 0
    while not found and i < len(L):
        if 2 ** X == L[i]:
            found = True
        else:
            i = i + 1
    if found:
        print('at index', i)
    else:
        print(X, 'not found')


def main():
    task_4()


if __name__ == '__main__':
    main()
