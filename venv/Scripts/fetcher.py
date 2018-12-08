import urllib3
import requests
import pandas as pd
import pandas_datareader.data as web
import chardet


class Fetcher:
    # code = ""

    def __init__(self, code):
        self.code = code
        # print ("fetch_data object init: %s" %__name__)

    def update(self):
        tmp = self.stock.iloc[0]
        self.stock.iloc[0] = tmp * 10
        print('\n----------------------------\n')
        print(self.stock.head(5))

    def drop(self):
        print(self.stock.drop('Adj Close', axis=1).head(5))
        print('\n----------------------------\n')
        print(self.stock.head(5))

    def fetch(self, start, end):
        self.stock = web.DataReader(self.code, "yahoo", start, end)
        print(self.stock.head(5))
        print('\n----------------------------\n')
        return self.stock

    @staticmethod
    def get_page(url):
        header = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Referer': r'https://www.jianshu.com/c/20f7f4031550?utm_medium=index-collections&utm_source=desktop',
            'Connection': 'keep-alive'
        }
        requests.packages.urllib3.disable_warnings()
        http = urllib3.PoolManager()
        try:
            raw_data = http.request('GET', url,  headers=header)
        except Exception as e:
            raise e
        finally:
            print(raw_data.status)  # 200

        # 获得html源码,utf-8解码
        # print(rawdata.data.decode())
        return raw_data


        # chardet.detect(rawdata)

        # print ("%.2f"%stock['High'][0])
        # print ("%.2f"%stock['High'][1])
        # print ("%.2f"%stock['High'][2])
        # print ("%.2f"%stock['High'][3])
        # print ("%.2f"%stock['High'][4])

        # print ('\n----------------------------\n')
        # print (stock.loc["2018-04-26":"2018-05-1"])

        # print ('\n----------------------------\n')
        # print (stock.tail(5))

        # print ('\n----------------------------\n')
        # print (stock.index)
        # print ('\n----------------------------\n')
        # print (stock.columns)
        # print ('\n----------------------------\n')
        # print (stock.shape)
        # print ('\n----------------------------\n')
        # print (stock.info())
        # print (stock.tail(5))
