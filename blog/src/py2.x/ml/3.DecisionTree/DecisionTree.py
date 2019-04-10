#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DecisionTree.py
@Time    :   2019/04/09 15:20:00
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   decisionTree
@github  :   https://github.com/xiaoming3526/ai-ming3526
'''

# here put the import lib
from __future__ import print_function
print(__doc__)
import operator
from math import log
from collections import Counter

'''
ctrl+alt+t
@description: 创建数据集
@param {None} 
@return: 返回数据集和对应的label标签
'''
def creatDataSet():
    '''
    |不浮出水面可以生存| 是否有脚蹼 |属于鱼类
    |1-是----------------------|-是------------|是
    |2-是---------------------  |-是------------|是
    |3-是---------------------  |-否------------|否
    |4-否---------------------  |-是------------|否
    |5-否---------------------  |-是------------|否
    '''
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

'''
@description: 计算给定数据集的香农熵
@param {type} 数据集
@return: 返回 每一组feature下的某个分类下，香农熵的信息期望
'''
def calcShannonEnt(dataSet):
    # -----------计算香农熵的第一种实现方式start--------------------------------------------------------------------------------
    #
    # numEntries = len(dataSet)
    # labelsCounts = {}
    # for featVec in dataSet:
    #     currentLabel = featVec[-1]
    #     if currentLabel not in labelsCounts.keys():
    #         labelsCounts[currentLabel] = 0
    #     labelsCounts[currentLabel] += 1
    # shannonEnt = 0.0
    # for key in labelsCounts:
    #     prob = float(labelsCounts[key])/numEntries
    #     shannonEnt -= prob * log(prob, 2)
    # -----------计算香农熵的第一种实现方式end--------------------------------------------------------------------------------
    # -----------计算香农熵的第二种实现方式start--------------------------------------------------------------------------------
     # -----------计算香农熵的第一种实现方式end--------------------------------------------------------------------------------

    # # -----------计算香农熵的第二种实现方式start--------------------------------------------------------------------------------
    # # 统计标签出现的次数
    label_count = Counter(data[-1] for data in dataSet)
    print(label_count)
    # # 计算概率
    probs = [float(p[1]) / len(dataSet) for p in label_count.items()]
    # # 计算香农熵
    shannonEnt = sum([-p * log(p, 2) for p in probs])
    # -----------计算香农熵的第二种实现方式end--------------------------------------------------------------------------------
    return shannonEnt

if __name__ == '__main__':
    myData,labels = creatDataSet()
    print(calcShannonEnt(myData))