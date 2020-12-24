# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:27:03 2020

@author: user
"""


def permute2(seq):
    if not seq:             # Тасование любой последовательности: генератор
        yield seq           # Пустая последовательность
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  # Удаление текущего узла
            for x in permute2(rest):   # Перестановка остальных
                yield seq[i:i+1] + x    # Добавление узла спереди


def main():
    S = '1234567890'
    X = permute2(S)
    input('Press any key...')
    with open('permutate.txt', 'w') as fout:
        for i in X: fout.write(i+'\n')
    return 0

if __name__ == '__main__':
    main()
