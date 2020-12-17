# -*- coding: utf-8 -*-
"""
Задания к Части 3
Created on Wed Dec 16 13:41:44 2020

@author: user
"""


def task1a(*arg):
    """
    Задание 1а. Напишите цикл for, который выводит код ASCII каждого \
    символа в строке по имени S.
    Для преобразования символа в целочисленный код ASCII \
    используйте встроенную функцию ord (символ).
    """
    print(arg[0])


def main():
    task1a('Test string')
    pass


if __name__ == '__main__':
    main()
