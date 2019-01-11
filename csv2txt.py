#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import os
import pandas as pd


def getFiles(path):
    files = os.listdir(path)
    # print(files)

    return files


def csv2txt(path='./time_zones', writeTo='./loc_json'):
    readPath = path
    if not readPath.endswith('/'):
        readPath += '/'
    writePath = writeTo
    if not writePath.endswith('/'):
        writePath += '/'
    files = getFiles(readPath)

    # 遍历所有csv文件，每个文件是一个时间区间的数据
    for file in files:
        df = pd.read_csv(readPath + '%s' % file)
        locs = df[['lng', 'lat']]
        # 遍历该csv文件的每一行，将经纬度数据转换为json可读的格式
        with open(writePath + '%s.txt' % file.split('.')[0], 'w') as f:
            for i in range(len(locs)):
                line = '{"lng":'+str(locs.iloc[i][0])+',"lat":'+str(locs.iloc[i][1])+'},\n'
                f.write(line)


if __name__ == '__main__':  
    csv2txt()
