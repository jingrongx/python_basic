#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import calendar

def loginfo(logString):
    # print now time
    print('%s: %s' % (datetime.datetime.now().strftime("%Y-%m-%d %X.%f"), logString))

def main():
    udisk = ['SanDisk', 'Kingston']
    loginfo(udisk)
    loginfo(udisk[0])
    loginfo(udisk[1])
    loginfo(udisk[-1])
    loginfo(udisk[-2])
    # add
    udisk.append('Lenovo')
    loginfo(udisk)

    # insert
    udisk.insert(1, 'HP')
    loginfo(udisk)

    # del
    udisk.pop()
    loginfo(udisk)
    udisk.pop(1)
    loginfo(udisk)

    # replace
    udisk[1] = 'Lenovo'
    loginfo(udisk)


    testListMix = ['desktop', 123, True]
    loginfo(testListMix)

    testListMul = ['python', 'java', ['jsp', 'php'], 'scheme']
    loginfo(len(testListMul))

    testListEmpty = []
    loginfo(testListEmpty)
    loginfo(len(testListEmpty))

if __name__ == '__main__':
    main()