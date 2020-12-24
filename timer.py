# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:22:02 2020

@author: Nikolay-PC
"""

# Файл timer.ру
I! И fl
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
Любительские инструменты для измерения времени выполнения вызовов функций.
Определяют суммарное время, лучшее время и лучшее суммарное время
п п п
import time, sys
timer = time-clock if sys.platform[:3] == 'win’ else time.time
def total(reps, func, * pargs, ** kargs) :
п я II
Total time to run func() reps times.
Returns (total time, last result)
Суммарное время выполнения функции func() reps раз
Возвращает (суммарное время, последний результат)
п и п
repslist = list (range (reps) ) # Вынести за пределы, уравнять Python 2.x, 3.x
start = timer () # Или perf—Counter/другая в Python 3.3+
for i in repslist:
ret = func( * pargs, ** kargs)
elapsed = timer() - start
return (elapsed, ret)
def bestof(reps, func, * pargs, ** kargs) :
»! П П
Quickest func() among reps runs.
Returns (best time, last result)
Самая быстрая функция func() среди reps запусков.
Возвращает (лучшее время, последний результат)
п п п
best = 2 ** 32 #136 лет представляется достаточным
for i in range (reps): # Использование range при измерении времени не учитывается
start = timer()
ret = func( * pargs, ** kargs)
elapsed = timer () - start # Или вызвать total () c reps=l
if elapsed < best: best = elapsed # Или добавить в список и найти min()
return (best, ret)
def bestoftotal(repsl, reps2, func, * pargs, ** kargs) :
П П If
Best of totals:
(best of repsl runs of (total of reps2 runs of func))
Лучшее суммарное время:
(лучшее время из repsl запусков (суммарное время reps2 запусков func))
п п п
return bestof(repsl, total, reps2, func, * pargs, ** kargs)