# -*- coding: utf-8 -*-
"""

"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
import os
THIS_DIR = os.path.realpath(os.path.dirname(__file__))

creditcard_raw = 'test_data/creditcard_raw.sas7bdat'

import pandas as pd
import matplotlib.pyplot as plt

print '1 读取数据，“id”列设为索引值'
df = pd.read_sas(creditcard_raw, index='id')

print '2 探索性数据分析'


print '2.1 判断重复性'
if df.duplicated().sum():
    print '2.2 有重复行，删除'
    df = df.drop_duplicates()
else:
    print '2.2 没有重复行'

print '2.2 描述性统计分析, 输出excel'
df.describe().to_excel('describe_of_creditcard_raw.xls')

print '2.3 画单列的频率条形统计图，输出png'
df_purpose = df.purpose
fig = df_purpose.value_counts().plot(kind='bar')
fig.set_title('frequency of 1000 creditcard users\' purpose')
plt.savefig('frequency_of_1000_creditcard_users_purpose.png')
