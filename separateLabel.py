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


def separateLabel(files=None, path='./data2', writeTo='./csv_separated_by_label'):
    readPath = path
    if not readPath.endswith('/'):
        readPath += '/'
    writePath = writeTo
    if not writePath.endswith('/'):
        writePath += '/'
    files = getFiles(path) if files is None else files # 否则用一个列表给出需要转换的文件

    # 遍历所有 csv 文件，每个文件是一天的数据
    for file in files:
        date = file.split('.')[0]
        df = pd.read_csv(readPath + file)
        df = df[['recitime','lng', 'lat', 'label']]

        # 根据标签值（0、1、2）对该 csv 文件的每一行分类
        df_0 = df[df['label']==0]
        df_1 = df[df['label']==1]
        df_2 = df[df['label']==2]

        # 将分类后的文件分别保存
        df_0.to_csv(writePath + date + '_0.csv', index=0)
        df_1.to_csv(writePath + date + '_1.csv', index=0)
        df_2.to_csv(writePath + date + '_2.csv', index=0)


if __name__ == '__main__':  
    separateLabel(writeTo='./csv_separated_by_label')
