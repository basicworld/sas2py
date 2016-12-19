# -*- coding: utf-8 -*-
"""

"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
# THIS_DIR = os.path.realpath(os.path.dirname(__file__))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print '0 载入数据'
sas_raw1 = 'test_data/profit.sas7bdat'
df1 = pd.read_sas(sas_raw1)
# print df1

print '1 分类变量的描述'
df_order_type = df1.order_type
describ = df_order_type.value_counts()
describ = pd.DataFrame(describ)
describ.plot.bar(title='order_type 对象的条形分布图')
plt.show()
describ['percent'] = describ.order_type / describ.order_type.sum() * 100
describ['cumsum_order_type'] = describ.order_type.cumsum()
describ['cumsum_percent'] = describ.percent.cumsum()
print describ


