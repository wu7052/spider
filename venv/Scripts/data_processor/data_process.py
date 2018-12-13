import pandas as pd
import numpy as np
import xlwt as wt
import xlrd as rd
from bs4 import BeautifulSoup
import re
import chardet
import sys
import io
from jsonpath import jsonpath
import json


class Processor:

    def __init__(self, code, frame):
        self.code = code
        self.data = frame

    def output(self, filename):
        self.data.to_excel(filename, sheet_name=self.code)


class Page_Parse:

    def __init__(self, page_data):
        self.page_data = page_data
        self.total_page = 0

    def parse(self, data=None):
        print("start to parse Page Data ...\n")

        if data == 'html':
            soup = BeautifulSoup(self.page_data.data, "html.parser")
            print(chardet.detect(self.page_data.data))
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
            print(self.page_data.data.decode("utf-8"))
            print(soup.find('div', {'class': 'table-responsive sse_table_T01 tdclickable'}))
        elif data == 'json':
            json_obj = json.loads(self.page_data)
            print("[parse json obj]:")
            company_code = jsonpath(json_obj, '$..pageHelp..COMPANY_CODE')  # 公司/A股代码
            company_abbr = jsonpath(json_obj, '$..pageHelp..COMPANY_ABBR')  # 公司/A股简称
            totalShares = jsonpath(json_obj, "$..pageHelp..totalShares")  # A股总资本
            totalFlowShares = jsonpath(json_obj, '$..pageHelp..totalFlowShares')  # A股流动资本
            totalPage = jsonpath(json_obj, '$..pageHelp.pageCount')
            self.total_page = totalPage
            """
            df = pd.DataFrame(company_code,
                              index=range(1, len(company_code) + 1),
                              columns=['A股代码'])

            df['A股简称'] = pd.Series(company_abbr, index=df.index)
            df['A股总资本'] = pd.Series(totalShares, index=df.index)
            df['A股流动资本'] = pd.Series(totalFlowShares, index=df.index)
            """

            stock_matix = [company_code, company_abbr ,totalShares, totalFlowShares]
            df = pd.DataFrame(stock_matix)
            df1 = df.T
            df1.rename(columns={0: 'ID', 1: 'Name',2: 'Total Shares',3: 'Flow Shares'}, inplace=True)
            #df1.sort_values(by=['Total Shares'], inplace=True)
            # print(df1.describe())
            #print(df1)
        else:
            print("[Type] shall be not None")
            return -1
# data = np.random.randn(40).reshape(8,5)

# frame = pd.DataFrame(data,columns=['A','B','C','D','E'])
