import datetime
from fetcher import *
from data_processor import Processor
from data_processor import Page_Parse
from database import DB_OP
import pandas as pd

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

page = 1

url = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback99887&' \
      'isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=' + str(page) + \
      '&pageHelp.beginPage=' + str(page) + '&pageHelp.pageSize=25&pageHelp.pageNo=' + str(page) + \
      '&pageHelp.endPage=' + str(page) + '1&_=1517320503161'

page_data_str = fd.get_page(url)
json_str = '{"content":' + page_data_str[19:-1] + '}'
# print(json_str)
page = Page_Parse(json_str)
stock_df = page.parse('json')
print("total page : {}".format(page.total_page))
print(stock_df)

try:
    db = DB_OP(host='127.0.0.1', db='stock', user='wx', pwd='5171013')
    for array in stock_df.get_values():
        sql = "select * from list_a where id ='"+array[0]+"'"
        # sql =  'select count(*) from list_a where id = \'%s\''%array[0]
        iCount = db.cursor.execute(sql) # 返回值，受影响的行数， 不需要 fetchall 来读取了
        # iCount= db.cursor.fetchone()
        if iCount == 0:
            print("Inserted\t[{0}==>{1}]".format(array[0], array[1]))
            sql ='insert into list_a ('id','name','total_shares','flow_shares','list_date') values (%s, %s, %f, %f, %s)'
            
        elif iCount == 1:
            print("Existed\t[{0}==>{1}]".format(array[0], array[1]))
        else:
            print("iCount == %d , what happended ???"% iCount)


    # cursor = db.DB_Connect()
    # data = db.cursor.fetchall()
    # print(data)
    db.cursor.close()
    db.handle.close()
except Exception as e:
    print('Err occured in DB operation')
    exit(-1)



# p_parse = Page_Parse(page_data)
# p_parse.parse()
