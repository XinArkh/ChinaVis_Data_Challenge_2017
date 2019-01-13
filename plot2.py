#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FuncFormatter
# import seaborn as sns; sns.set()
# import seaborn as sns; sns.set_style('whitegrid')


def getFiles(path):
    files = os.listdir(path)
    # print(files)

    return files


def formatnum(x, pos):
    return '$%.1f$x$10^{4}$' % (x/10000)


def formatdate(files, num):
    return files[num][4:6] + '-' + files[num][6:8]


def formathour(num):
    return '%02d' % num + ':00'


nums = np.zeros((63, 24))

times = getFiles('./csv_separated_by_time')
dates = getFiles('./data')

for i in range(len(times)):
    df = pd.read_csv('./csv_separated_by_time/'+times[i])
    for j in range(len(dates)):
        date = int(dates[j].split('.')[0])
        nums[j, i] = np.sum(df['date']==date)

# 图 1：完整的 63×24 矩阵；图 2：去掉异常偏高日期（2.23、3.4、3.5）后的矩阵
fig, ax = plt.subplots(1,2)
for i in range(len(ax)):
    # 在图 2 中去掉异常日期
    if i == 1:
        nums[0] = 0
        nums[9] = 0
        nums[10] = 0

    # 绘制并设置格式
    c0 = ax[i].matshow(nums)  # 绘制矩阵图
    fig.colorbar(c0, ax=ax[i], format=FuncFormatter(formatnum))  # 添加颜色条
    ax[i].xaxis.set_ticks_position('bottom')  # 将 x 轴移到下面（原来在上面）
    ax[i].invert_yaxis()  # 反转 y 轴（原来方向向下）

    # 设置 x 轴刻度
    hours = [2, 7, 12, 17, 22]
    ax[i].set_xticks(hours)
    ax[i].set_xticklabels([formathour(h) for h in hours])
    # 设置 y 轴刻度
    days = [2, 22, 42, 62]
    ax[i].set_yticks(days)
    ax[i].set_yticklabels([formatdate(dates, d)for d in days])

plt.show()