# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 21:00:38 2020

@author: Nikolay-PC
"""

class Person():

    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay


if __name__ == '__main__':
    bob = Person('Nik')
    joe = Person('Dick', 'worker', 123)
    don = Person('Anna', 'hustler', '$1000')

    print(bob.name)
    print(joe.job)
    print(don.pay)
