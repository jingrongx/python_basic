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


def loops(a):
    for i in a:
        if i<3:
            r_log.logger.info('a<3')
        else:
            r_log.logger.info('a>=3')

    sum = 0
    for x in range(101):
        sum = sum + x
    r_log.logger.info(sum)

    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    r_log.logger.info(sum)

    name = ["a", "b", "c"]
    for x in name:
        message = "Hello: " + x
        r_log.logger.info(message)


def main():
    # 'application' code
    r_log.logger.debug('debug message')
    r_log.logger.info('info message')
    r_log.logger.warning('warn message')
    r_log.logger.error('error message')
    r_log.logger.critical('critical message')
    l = [1, 2, 3]
    loops(l)


if __name__ == '__main__':
    main()