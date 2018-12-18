import datetime
from fetcher import *
from data_processor import Processor
from data_processor import Page_Parse
from database import DB_OP
import pandas as pd
import logging

# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename='spider_all.log', level=logging.DEBUG, format=LOG_FORMAT)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")
fh = logging.FileHandler('spider_debug.log',encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger = logging.getLogger('spider')
logger.setLevel(logging.ERROR)
logger.addHandler(fh)
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')

start = datetime.datetime(2018, 1, 15)
end = datetime.date.today()
code = "600797.SS"
# print (__name__)

fd = Fetcher(code)

# 读取股票交易数据
# frame = fd.fetch(start, end)

# 处理股票数据，输出到 excel
# ps = Processor(code, frame)
# ps.output(r'D:\stock.xls')
# fd.drop()
# fd.update()

# 读取web页面
# page_data = fd.get_page(r'http://www.sse.com.cn/assortment/stock/list/share/')

page_counter = 1
try:
    db = DB_OP(host='127.0.0.1', db='stock', user='wx', pwd='5171013')

    while(page_counter<59):
        url = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback99887&' \
              'isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=' \
              + str(page_counter) + '&pageHelp.pageSize=25&pageHelp.pageNo=' + str(page_counter) + \
              '&pageHelp.endPage=' + str(page_counter) + '1&_=1517320503161'+ str(page_counter)

        page_data_str = fd.get_page(url)
        json_str = '{"content":' + page_data_str[19:-1] + '}'
        # print(json_str)
        page = Page_Parse(json_str)
        stock_df = pd.DataFrame()
        stock_df = page.parse('json')
        print("total page : {0}==> cur page : {1}".format(page.total_page, page_counter))
        logger.debug(stock_df)

        for array in stock_df.get_values():
            sql = "select * from list_a where id ='"+array[0]+"'"
            # sql =  'select count(*) from list_a where id = \'%s\''%array[0]
            iCount = db.cursor.execute(sql) # 返回值，受影响的行数， 不需要 fetchall 来读取了
            if iCount == 0:
                sql ="insert into list_a (id, name, total_shares, flow_shares, list_date) values (%s, %s, %s ,%s, %s)"
                logger.debug("Insert id={0}, name={1}, t_shares={2}, f_shares={3}, date={4}".
                             format(array[0], array[1], array[2], array[3],array[4]))
                db.cursor.execute(sql,(array[0], array[1], float(array[2]), float(array[3]), array[4]))
                db.handle.commit()
            elif iCount == 1:
                logger.debug("Existed\t[{0}==>{1}]".format(array[0], array[1]))
            else:
                logger.debug("iCount == %d , what happended ???"% iCount)

        page_counter += 1

    # cursor = db.DB_Connect()
    # data = db.cursor.fetchall()
    # print(data)
    db.cursor.close()
    db.handle.close()
except Exception as e:
    print('Err occured in DB operation {}'.format(e))
    exit(-1)



# p_parse = Page_Parse(page_data)
# p_parse.parse()
