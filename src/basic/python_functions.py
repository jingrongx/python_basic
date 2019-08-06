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

# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person_1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    r_log.logger.info(('name:', name, 'age:', age, 'other:', kw))

# 命名关键字参数时，如果没有可变参数，就必须加一个*作为特殊分隔符。
def person_2(name, age, *, city, job):
    r_log.logger.info((name, age, city, job))


# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
def f1(a, b, c=0, *args, **kw):
    r_log.logger.info(('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw))


def f2(a, b, c=0, *, d, **kw):
    r_log.logger.info(('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw))


def product(*num):
    if len(num) == 0:
        raise TypeError
    elif len(num) == 1:
        return num[0]
    else:
        x = 1
        for y in num:
            x = x * y
        return x


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
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person_1('Jack', 24, **extra, addr='Chaoyang', zipcode=123456)
    person_2('Jack', 24, city='Beijing', job='Engineer')
    args = (1, 2, 3, 4)
    kw = {'d': 99, 'x': '#'}
    f1(*args, **kw)
    args = (1, 2, 3)
    kw = {'d': 88, 'x': '#'}
    f2(*args, **kw)
    r_log.logger.info(product(1,2,3))

if __name__ == '__main__':
    main()