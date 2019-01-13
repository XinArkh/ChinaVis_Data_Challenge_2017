#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FuncFormatter
import seaborn as sns; sns.set()
# import seaborn as sns; sns.set_style('whitegrid')


def getFiles(path):
    files = os.listdir(path)
    # print(files)

    return files


def formatnum(x, pos):
    return '$%.1f$x$10^{3}$' % (x/1000)


def formatdate(files, num):
    print(files)
    return files[num][4:6] + '-' + files[num][6:8]


def formathour(num):
    return '%02d' % num + ':00'


nums = np.zeros((3, 3, 25))  # 类、天、时

times = getFiles('./csv_separated_by_time_3days')
dates = ['20170227.csv', '20170326.csv', '20170404.csv']

for i in range(len(times)):
    df = pd.read_csv('./csv_separated_by_time_3days/'+times[i])
    for j in range(len(dates)):
        date = int(dates[j].split('.')[0])
        # nums[j, i] = np.sum(df['date']==date)
        df_date = df[df['date']==date]
        for k in [0, 1, 2]:
            nums[k, j, i] = np.sum(df_date['label']==k)

nums[..., 24] = nums[..., 23]

for fi in [0, 1, 2]:
    fig = plt.figure(fi)

    # n = nums[:, fi, :]  # 每一个 Figure 是一天的三种短信变化
    n = nums[fi, ...]  # 每一个 Figure 是一种短信在三个日期的变化
    plt.plot(n.T)
    ax = plt.gca()
    # ax.legend(['金融欺诈类', '骚扰广告类', '非法广告类'], prop={'family':'SimHei'}, fontsize='large')
    ax.legend(['02-27', '03-26', '04-04'], prop={'family':'SimHei'}, fontsize='large')

    # 设置 x 轴
    ax.set_xlim([0, 24])
    hours = [2, 7, 12, 17, 22]
    ax.set_xticks([xt-0.5 for xt in hours])
    ax.set_xticklabels([formathour(h) for h in hours])

    # 设置 y 轴刻度
    ax.set_ylim([-2e2, 5.99e3])
    formatter = FuncFormatter(formatnum)
    ax.yaxis.set_major_formatter(formatter)

    # 坐标轴端点文字
    plt.text(-1, 6.15e3, '短信条数/条', fontproperties='SimHei')
    plt.text(24.3, -0.4e3, '时间', fontproperties='SimHei')

plt.show()