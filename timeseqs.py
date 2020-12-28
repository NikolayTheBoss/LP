# -*- coding: utf-8 -*-
"""
Проверка относительной скорости итерационных альтернатив.
Файл timeseqs.py
"""


import sys
import timer

reps = 100
repslist = list(range(reps))


def forLoop() -> list:
    """Генерирует список циклом и добавлением append."""
    res = []
    for i in repslist:
        res.append(abs(i))
    return res


def listComp() -> list:
    """Генерирует список включением списка."""
    return [abs(i) for i in repslist]


def mapList() -> list:
    """Генерирует список отображением map"""
    return list(map(abs, repslist))


def genExp() -> list:
    """Генерирует список проходом цикла"""
    return list(abs(i) for i in repslist)


def genFunc() -> list:
    """Генерирует список преобразованием геренатора в list"""
    def gen():
        for i in repslist:
            yield abs(i)
    return list(gen())


if __name__ == '__main__':
    for testFunc in (forLoop, listComp, mapList, genExp, genFunc):
        (bestof, result) = timer.bestoftotal (testFunc)
        print ('%-9s: %.5f => [%s...%s]' % 
           (testFunc.__name__ , bestof, result[0], result[-1]))
