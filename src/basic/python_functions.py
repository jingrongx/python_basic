#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import math

class r_log():
    # create logger
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create file handler and set level to debug
    fh = logging.FileHandler('example.log', mode='a')
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add formatter to fh
    fh.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # add fh to logger
    logger.addHandler(fh)


def build_in_functions(*args):
    for i in args:
        r_log.logger.info("%s abs is: %s" % (i, abs(i)))
        r_log.logger.info("%s hex is: %s" % (i, hex(i)))

    maxNum = max(args)
    r_log.logger.info("The max num is: %s" % (maxNum))

def custom_functions(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    x = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    y = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x, y


# 把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def power(x, n=2):
    # 只能计算正整数次幂
    # s = 1
    # while n > 0:
    #     n = n - 1
    #     s = s * x

    # 可以计算任意数次幂
    s = x ** n
    return s

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 定义可变参数，在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def main():
    # 'application' code
    r_log.logger.debug('debug message')
    r_log.logger.info('info message')
    r_log.logger.warning('warn message')
    r_log.logger.error('error message')
    r_log.logger.critical('critical message')
    a=-1
    b=-100
    c=-9
    d=10
    build_in_functions(a, b, c, d)
    r_log.logger.info(custom_functions(a))
    r_log.logger.info(custom_functions(d))
    nop()
    r = move(100, 100, 60, math.pi / 6)
    r_log.logger.info(r)
    r_log.logger.info(quadratic(a, b, c))
    r_log.logger.info(power(3))
    r_log.logger.info(power(3, 3/7))
    r_log.logger.info(add_end([]))
    r_log.logger.info(add_end([1,2]))
    r_log.logger.info(calc(*[1,2]))
    r_log.logger.info(calc(1,2))

if __name__ == '__main__':
    main()