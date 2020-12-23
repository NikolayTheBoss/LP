# -*- coding: utf-8 -*-
""" Это тестовый файл по открытию файлов"""


def main(*arg):
    with open(*arg, 'w') as fout:
        fout.write("Hello, World!")
    return None


def read_hello(*arg):
    path = arg[0]
    for fline in open(path, 'r'):
        print(fline)


if __name__ == '__main__':
    finput = input("Enter the path to the File: ")
    print(finput)
    main(finput)
    read_hello("c:\\users\\user\\text\\test.txt")
    while True:
        reply = input('Enter text:')
        if reply == 'stop':
            break
        print(reply.upper())
        print(reply.upper())
