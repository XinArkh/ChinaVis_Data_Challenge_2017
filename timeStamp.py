#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import csv
import time
import pandas as pd


def getFiles(path):
    files = os.listdir(path)
    # print(files)

    return files


def createTimeStamps(num, date):
    delta = 24 / num
    assert delta == int(delta), 'time interval invlaid'
    delta = int(delta)

    time_stamps = []
    H = 0
    while H < 24:
        t = str(date) + '-%s' % H
        time_stamp = int(time.mktime(time.strptime(t, '%Y%m%d-%H')))
        time_stamp *= 1000  # csv文件中时间戳是13位，末尾多三个0
        time_stamps.append(time_stamp)
        H += delta

    return time_stamps


def timeIntervals(num=24, path='./data'):
    files = getFiles(path)

    # 遍历所有csv文件，每个文件是一天的数据
    for i in range(len(files)):
        date = files[i].split('.')[0]
        time_stamps = createTimeStamps(num, date)
        df = pd.read_csv('./data/%s.csv' % date)

        intervals = [[] for _ in range(len(time_stamps))]  # 不要用 [[]] * num 初始化，会使得所有[]共享内存
        # 遍历该csv文件的每一行，对每个时间区间内的点分类
        for j in range(len(df)):
            ts = df.ix[j, 'recitime']
            k = 0
            while ts > time_stamps[k]:
                k += 1
                if k == len(time_stamps):
                    break
            contents = list(df.ix[j, ['recitime','lng', 'lat']])
            contents.append(int(date))
            intervals[k-1].append(contents)

        for n in range(len(time_stamps)):
            if not os.path.exists('./time_intervals/time%s.csv' % n):
                with open('./time_intervals/time%s.csv' % n, 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(['recitime','lng', 'lat', 'date'])
            with open('./time_intervals/time%s.csv' % n, 'a') as f:
                writer = csv.writer(f)
                writer.writerows(line for line in intervals[n])


if __name__ == '__main__':  
    timeIntervals(num=24, path='./data')
