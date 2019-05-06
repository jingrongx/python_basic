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


def main():
    # 'application' code
    r_log.logger.debug('debug message')
    r_log.logger.info('info message')
    r_log.logger.warn('warn message')
    r_log.logger.error('error message')
    r_log.logger.critical('critical message')

if __name__ == '__main__':
    main()