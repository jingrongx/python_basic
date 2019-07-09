#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

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
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add formatter to fh
    fh.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # add fh to logger
    logger.addHandler(fh)


def conditions(*args):
    # if <条件判断1>:
    #     <执行1>
    # elif <条件判断2>:
    #     <执行2>
    # elif <条件判断3>:
    #     <执行3>
    # else:
    #     <执行4>
    for i in args:
        if i<3:
            r_log.logger.info('a<=3')
        else:
            r_log.logger.info('a>3')


def main():
    # 'application' code
    r_log.logger.debug('debug message')
    r_log.logger.info('info message')
    r_log.logger.warning('warn message')
    r_log.logger.error('error message')
    r_log.logger.critical('critical message')
    a=1
    b=2
    c=3
    d=4
    e=5
    f=6
    g=7
    h=int(input('h: '))
    conditions(a, b, c, d, e, f, g, h)

if __name__ == '__main__':
    main()