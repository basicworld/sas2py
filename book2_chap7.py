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
import matplotlib.pyplot as plt

print '0 载入数据'
sas_raw1 = 'test_data/sale.sas7bdat'
columns = pd.read_sas(sas_raw1).columns
df1 = pd.read_sas(sas_raw1, encoding='gb2312')
df1.columns = columns
print df1

print '\n1 饼形图-各市场销量占比'
df1_year = df1.pivot('year', 'market', 'sale')
# df1_market = df1_year.T
sale_market = df1_year.sum()
print sale_market
colors = ['red', 'yellowgreen', 'lightskyblue', 'blue']
pie = sale_market.plot.pie(colors=colors, autopct='%3.1f%%')
pie.set_title('各市场销量比例图')
plt.axis('equal')
plt.savefig('pics/book2_chap6_pie.jpg')
plt.delaxes()

print '\n2 条形图、柱形图-各市场销量'
barh = sale_market.sort_values().plot.barh(color='g')
barh.set_title('各市场销量条形图')
plt.savefig('pics/book2_chap6_barh.jpg')
plt.delaxes()

bar = sale_market.sort_values().plot.bar(color='g')
bar.set_title('各市场销量柱形图')
plt.savefig('pics/book2_chap6_bar.jpg')
plt.delaxes()


print '\n3 折线图-每年销量变化'
df1_market = df1_year.T
sale_year = df1_market.sum()
print sale_year
line = sale_year.plot.line(color='g')
line.set_title = '折线图-每年销量变化'
plt.xticks(sale_year.index.astype(int), sale_year.index.astype(int))
plt.savefig('pics/book2_chap6_line.jpg')
plt.delaxes()

print '\n4 雷达图-个人胜任素质图示'
labels = np.array(['组织计划', '主动性', '成就导向', '数字分析', '承压能力'])
data = np.array([6, 9, 8, 9, 9])
data_len = len(data)

angles = np.linspace(0, 2*np.pi, data_len, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))

fig = plt.figure()
# 使用极坐标
ax = fig.add_subplot(111, polar=True)
# 标注坐标，黑色实线，线宽1
ax.plot(angles, data, 'ko-', linewidth=1)
# 填充颜色 绿色 透明度0.6
ax.fill(angles, data, facecolor='g', alpha=0.6)
# 设置label
ax.set_thetagrids(angles*180/np.pi, labels, fontproperties='SimHei')
ax.set_title('胜任素质雷达图')
ax.set_rlim(0, 10)
ax.grid(True)
plt.savefig('pics/book2_chap6_radar.jpg')
plt.delaxes()
