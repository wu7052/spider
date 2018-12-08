import pandas as pd
import numpy as np
import xlwt as wt
import xlrd as rd
from bs4 import BeautifulSoup
import re
import chardet
import sys
import io

class Processor:

    def __init__(self, code, frame):
        self.code = code
        self.data = frame

    def output(self, filename):
        self.data.to_excel(filename, sheet_name=self.code)


class Page_Parse:

    def __init__(self, page_data):
        self.page_data = page_data

    def parse (self):
        print ("start to parse Page Data ...\n")
        soup = BeautifulSoup(self.page_data.data, "html.parser")
        print(chardet.detect(self.page_data.data))
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
        print(self.page_data.data.decode("utf-8"))
        #open('d:\\2countries2.html', 'w').write(str(self.page_data.data.decode("gbk ")))

        #for tag in  soup.find_all('tbody' > 'tr' > 'td' > 'a' , href = re.compile(r'/assortment/stock/list/info/company/index.shtml\?COMPANY_CODE=')):
        #   print (tag.string )
        print (soup.find('div',{'class':'table-responsive sse_table_T01 tdclickable'}))

#data = np.random.randn(40).reshape(8,5)

#frame = pd.DataFrame(data,columns=['A','B','C','D','E'])