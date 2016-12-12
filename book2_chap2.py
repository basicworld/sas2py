# -*- coding: utf-8 -*-
"""

"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
import os
THIS_DIR = os.path.realpath(os.path.dirname(__file__))

filename = 'test_data/card1.sas7bdat'

from sas7bdat import SAS7BDAT
import pandas as pd

# rows = []
# with SAS7BDAT(filename) as f:
#     for row in f:
#         print row[-1]
#         rows.append(row)
# df = pd.DataFrame(rows)
# print df

dat = pd.read_sas(filename)
print dat
