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
    loginfo(UDisk)

    tEmpty = ()
    loginfo(tEmpty)

    # tuple tNum
    tNum = (1,)
    loginfo(tNum)

    # int num
    num = (1)


if __name__ == '__main__':
    main()