# -*- coding: utf-8 -*-
# Файл timer.ру
"""
Любительские инструменты для измерения времени выполнения вызовов функций.
Определяют суммарное время, лучшее время и лучшее суммарное время
"""

import time
import sys
from permute import permute2

timer = time.perf_counter if sys.platform[:3] == 'win' else time.time


def total(reps, func, * pargs, ** kargs):
    """
    Суммарное время выполнения функции func() reps раз
    Возвращает (суммарное время, последний результат)
    """
    repslist = list (range(reps))     # Уравнять Python 2.x, 3.x
    start = timer()                   # Или perf—Counter/другая в Python 3.3+
    for i in repslist:
        ret = func(* pargs, ** kargs)
        elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps, func, * pargs, ** kargs):
    """
    Самая быстрая функция func() среди reps запусков.
    Возвращает (лучшее время, последний результат)
    """
    best = 2**32          # 136 лет представляется достаточным
    for i in range(reps):  # range при измерении времени не учитывается
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start   # Или вызвать total() c reps=l
        if elapsed < best:
            best = elapsed   # Или добавить в список и найти min()
    return (best, ret)


def bestoftotal(reps1, reps2, func, * pargs, ** kargs):
    """
    Лучшее суммарное время:
    (лучшее время из reps1 запусков (суммарное время reps2 запусков func))
    """
    return bestof(reps1, total, reps2, func, * pargs, ** kargs)


if __name__ == '__main__':
    print(total(1, permute2('123')))