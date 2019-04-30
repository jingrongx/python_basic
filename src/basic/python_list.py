#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import calendar

def output(info):
    print(info)
    # print now time
    print(datetime.datetime.now().strftime("%Y-%m-%d %X.%f"))

def main():
    udisk = ['SanDisk', 'Kingston']
    output(udisk)
    output(udisk[0])
    output(udisk[1])

if __name__ == '__main__':
    main()