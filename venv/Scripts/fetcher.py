import urllib3
import requests
import pandas as pd
import pandas_datareader.data as web
import chardet
import logging

class Fetcher:
    # code = ""

    def __init__(self, code):
        self.code = code
        # print ("fetch_data object init: %s" %__name__)

    def update(self):
        tmp = self.stock.iloc[0]
        self.stock.iloc[0] = tmp * 10
        # logging.debug('[fetcher]\n----------------------------\n')
        # logging.debug('[fetcher]'+self.stock.head(5))

    def drop(self):
        pass
        # logging.debug('[fetcher]'+self.stock.drop('Adj Close', axis=1).head(5))
        # logging.debug('\n----------------------------\n')
        # logging.debug('[fetcher]'+self.stock.head(5))

    def fetch(self, start, end):
        self.stock = web.DataReader(self.code, "yahoo", start, end)
        # logging.debug('[fetcher]'+self.stock.head(5))
        # logging.debug('[fetcher]\n----------------------------\n')
        return self.stock

    def get_page(self, url):
        header = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Referer': r'https://www.jianshu.com/c/20f7f4031550?utm_medium=index-collections&utm_source=desktop',
            'Connection': 'keep-alive'
        }

        headers = {
            'Cookie': 'yfx_c_g_u_id_10000042=_ck18012900250116338392357618947; VISITED_MENU=%5B%228528%22%5D; yfx_f_l_v_t_10000042=f_t_1517156701630__r_t_1517314287296__v_t_1517320502571__r_c_2',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/'
            }

        requests.packages.urllib3.disable_warnings()
        http = urllib3.PoolManager()
        try:
            raw_data = http.request('GET', url,  headers=headers)
        except Exception as e:
            raise e
        finally:
            # logging.debug('[fetcher]{}'.format(raw_data.status)) # 200
            pass

        # 获得html源码,utf-8解码
        # logging.debug(chardet.detect(raw_data.data))
        # logging.debug(type(raw_data.data))
        #print(chardet.detect(unicode))
        #print(type(raw_data.data))
        unicode = raw_data.data.decode("utf-8")
        # print(type(unicode))
        
        return unicode

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
