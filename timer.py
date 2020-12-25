# -*- coding: utf-8 -*-
# Файл timer.ру
"""
Любительские инструменты для измерения времени выполнения вызовов функций.
Определяют суммарное время, лучшее время и лучшее суммарное время
"""

import time
import sys
# from permute import permute2

timer = time.perf_counter


def total(func, *pargs, _reps=1000, **kargs):
    """
    Суммарное время выполнения функции func() reps раз

    Возвращает (суммарное время, последний результат)
    """
    start = timer()                   # Или perf—Counter/другая в Python 3.3+
    for i in range(_reps):
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
    return (elapsed, ret)


def bestof(func, *pargs, _reps=5, **kargs):
    """
    Самая быстрая функция func() среди _reps запусков.

    По-умолчанию    
    Возвращает (лучшее время, последний результат)
    """
    best = 2**32          # 136 лет представляется достаточным
    for i in range(_reps):  # range при измерении времени не учитывается
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start   # Или вызвать total() c reps=l
        if elapsed < best:
            best = elapsed   # Или добавить в список и найти min()
    return (best, ret)


def bestoftotal(func, *pargs, _reps=5, **kargs):
    """
    Лучшее суммарное время:
    (лучшее время из reps1 запусков (суммарное время reps2 запусков func))
    """
    return min(total(func, *pargs, **kargs) for i in range(_reps))
