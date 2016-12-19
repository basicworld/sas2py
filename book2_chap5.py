# -*- coding: utf-8 -*-
"""

"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
THIS_DIR = os.path.realpath(os.path.dirname(__file__))

import pandas as pd
# import numpy as np

sas_raw = 'test_data/zhaibiao.sas7bdat'
df = pd.read_sas(sas_raw)
print df

print '\n1 数据预处理-拆分列'
df = df.pivot('id', 'month', 'sale')
print df

print '\n2 计算新变量-六个月销售总收入'
df['total'] = df.sum(1)
print df

print '\n3 堆叠列'
print df.stack()

print '\n4 转置列'
print df.T

print '\n5 对列重编码-总业绩超过600的为优秀，其他为合格'
df['total_group'] = df.total.apply(lambda x: '优秀' if x >= 600 else '合格')
print df

print '\n6 标准化'
print '6.1 最大最小标准化'
max_total = df.total.max()
min_total = df.total.min()
trans_xi = lambda x: (x - min_total) / (max_total - min_total)
df['norm1'] = df.total.apply(trans_xi)
print df

print '6.2 zscore标准化'
mean_total = df.total.mean()
std_total = df.total.std()
trans_xi = lambda x: (x - mean_total) / std_total
df['norm2'] = df.total.apply(trans_xi)
print df

print '6.3 小数定标标准化'
max_total = df.total.max()
def get_j(xi, j=0):
    """
    得到小数定标标准化的j
    """
    if xi / float(10 ^ j) <= 1:
        return j
    else:
        return get_j(xi, j+1)

j = get_j(max_total)
print max_total / float(10 ^ j)

df['norm3'] = df.total.apply(lambda x: x / float(10 ^ j))
print df
