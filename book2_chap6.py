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

print '0 载入数据'
sas_raw1 = 'test_data/card1.sas7bdat'
sas_raw2 = 'test_data/card2.sas7bdat'
df1 = pd.read_sas(sas_raw1)
df2 = pd.read_sas(sas_raw2)
print df1
print df2

print '1 纵向连接'
print '1.1 纵向连接-不删除重复值'
print pd.concat([df1, df2], axis=0)
print '1.2 纵向连接-保留第一个重复值'
print pd.concat([df1, df2], axis=0).drop_duplicates(keep='first')


print '2 横向连接'
# pd.merge()
print df2.merge(df1,left_on='card_id',right_on='card_id')  # 空


