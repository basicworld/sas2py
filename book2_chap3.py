# -*- coding: utf-8 -*-
"""

"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
import os
THIS_DIR = os.path.realpath(os.path.dirname(__file__))
import time
creditcard_raw = 'test_data/creditcard_raw.sas7bdat'

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
print '\n1 读取数据，“id”列设为索引值'
df = pd.read_sas(creditcard_raw, index='id')

print '\n1.1 保存为excel便于查看'
df.to_excel('creditcard_raw.xls')
# sys.exit()

print '\n2 探索性数据分析'
print '\n2.1 判断重复性'
if df.duplicated().sum():
    print '\n2.2 有重复行，删除'
    df = df.drop_duplicates()
else:
    print '\n2.2 没有重复行'

print '\n2.2 描述性统计分析, 输出excel'
df.describe().to_excel('describe_of_creditcard_raw.xls')

print '\n2.3 画单列的频率条形统计图，输出png'
df_purpose = df.purpose
fig = df_purpose.value_counts().sort_index().plot(kind='bar')
fig.set_title('frequency of 1000 creditcard users\' purpose')
plt.savefig('frequency_of_1000_creditcard_users_purpose.png')

plt.delaxes(fig)
# del fig

print '\n3 类别变量的清理，以JOB1列为例'
df_job1 = df.JOB1
print '\n3.1 描述统计'
print '\n3.1.1 总体数据描述'
print 'null    %s' % df_job1.isnull().sum()
print df_job1.describe()
print '\n3.1.2 频率数据描述'
print df_job1.value_counts().describe()
print '\n3.2 画描述统计条形图'
fig2 = df_job1.value_counts().sort_index().plot(kind='bar')
fig2.set_title('frequency of 1000 creditcard users\' job')
plt.savefig('frequency_of_1000_creditcard_users_job.png')
plt.delaxes(fig2)

print '\n3.3 job1列按信用评级good_bad来分组，描述结果如下'
df_job1_grouped = df_job1.groupby(df.good_bad)
print df_job1_grouped.describe()

print '\n3.4 job1列去掉空值，并只选取信用评级为good的值'
df_job1_good = df_job1_grouped.get_group('good')
df_job1_good_notnull = df_job1_good[df_job1_good.notnull()]
print df_job1_good_notnull.describe()
print df_job1_good_notnull.value_counts()

print '\n4 数值型变量的清理，分析变量amount，分类变量employed1'
df_amount_groupby_employed1 = df.amount.groupby(df.employed1)
# df_employed1.sort_index()
print '\n4.1 首先进行描述性统计'
print '4.1.1 频率统计'
print df_amount_groupby_employed1.count()
print '4.1.2 均值统计'
print df_amount_groupby_employed1.mean()
print '4.1.3 标准差统计'
print df_amount_groupby_employed1.std()

print '4.1.4 最大值统计'
print df_amount_groupby_employed1.max()
print '4.1.5 缺失值统计'
print df_amount_groupby_employed1.apply(lambda x: x.isnull().sum())
# print '4.1.5 四分位下限'  # todo 转化为箱线图的下线
# print df_amount_groupby_employed1.apply(lambda x: eval(pd.cut(x.values,4).categories[0].replace('(','['))[-1])
# print '4.1.5 四分位上线'
# print df_amount_groupby_employed1.apply(lambda x: eval(pd.cut(x.values,4).categories[-1].replace('(','['))[0])
print '4.1.6 箱线图'
def box_plot(data):
    data.plot(kind='box')
    plt.savefig('box_plot_%s.png' % time.time())
    plt.delaxes()
    time.sleep(1)
df_amount_groupby_employed1.apply(box_plot)

print '\n5 正态分布验证，以amount数据为例'
df_amount = df.amount[df.amount.notnull()]
print '\n5.1 峰度sk'
print df_amount.skew()
print '\n5.2 偏度k'
print df_amount.kurt()
print '\n5.3 正太检验。需要去掉空值先'
statistic, p = stats.normaltest(df_amount.values)
if p < 0.05:
    print '\tnot normal'
else:
    print '\tcan not reject its normalize'
print '\n5.4 直方图'
fig5 = df_amount.hist(bins=18, alpha=0.3, color='k', normed=False)
df_amount.plot(kind='kde', style='k--', secondary_y=True)
fig5.set_title('hist of amount')
plt.savefig('hist_of_amount.png')
plt.delaxes()
