# -*- coding: utf-8 -*-
"""

"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
THIS_DIR = os.path.realpath(os.path.dirname(__file__))

import pandas as pd
import numpy as np

creditcard_raw = 'test_data/creditcard_raw.sas7bdat'
df = pd.read_sas(creditcard_raw, index='id')

print '1 数据筛选'

print '1.1 筛选amount的非缺失值'
df = df[df.amount.notnull()]
print '1.2 按照客户信用good_bad进行排序，输出到excel'
tmp = df.sort_values('good_bad')
tmp.to_excel('df_amount_not_null_sort_goodbad.xls')

print '\n2 排序和求秩'
print '2.1 按amount排序，输出到excel'
tmp2 = df.sort_values('amount')
tmp2.to_excel('df_sort_amount.xls')

print '2.2 求秩和抽取数据，选取amount列，\n 分别抽取信用等级good和bad的前10数据'
# 也可以使用df.rank
print df[df.good_bad == 'good'].sort('amount', ascending=False).head(10)
print df[df.good_bad == 'bad'].sort('amount', ascending=False).head(10)

print '\n3 抽样'
print '3.1 把信用等级good_bad作为抽样层变量，进行分层抽样，每层随机抽取10个'
samper = lambda x: np.random.randint(0, len(x)-1, 10)
df_good = df[df.good_bad == 'good']
print df_good.take(samper(df_good))

df_bad = df[df.good_bad == 'bad']
print df_bad.take(samper(df_bad))

print '\n4 按消费目的purpose做消费金额amount的汇总'
print df[['amount', 'purpose']].groupby('purpose').sum()
