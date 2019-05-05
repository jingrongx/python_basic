#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import calendar

def loginfo(logString):
    # print now time
    print('%s: %s' % (datetime.datetime.now().strftime("%Y-%m-%d %X.%f"), logString))

def main():
    UDisk = ('SanDisk', 'Kingston')
    loginfo(", ".join(UDisk))

    tEmpty = ()
    loginfo(tEmpty)

    # tuple tNum
    tNum = (1,)
    loginfo(tNum)

    # int num
    num = (1)

    # tuple & list
    UDisk = ('SanDisk', 'Kingston', ['Lenovo', 'agio'], 'intel')
    loginfo(UDisk)
    UDisk[2][0] = '1'
    UDisk[2][1] = '2'
    loginfo(UDisk)


if __name__ == '__main__':
    main()