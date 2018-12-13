import datetime
from fetcher import *
from data_processor import Processor
from data_processor import Page_Parse



start = datetime.datetime(2018, 1, 15)
end = datetime.date.today()
code = "600797.SS"
# print (__name__)

fd = Fetcher(code)

#读取股票交易数据
#frame = fd.fetch(start, end)

#处理股票数据，输出到 excel
#ps = Processor(code, frame)
#ps.output(r'D:\stock.xls')
# fd.drop()
#fd.update()

#读取web页面
# page_data = fd.get_page(r'http://www.sse.com.cn/assortment/stock/list/share/')

page = 1

url='http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback99887&' \
    'isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize='+str(page)+\
    '&pageHelp.beginPage='+str(page)+'&pageHelp.pageSize=25&pageHelp.pageNo='+str(page)+'&pageHelp.endPage='+str(page)+'1&_=1517320503161'

page_data_str = fd.get_page(url)
json_str = '{"content":'+ page_data_str[19:-1] +'}'
print(json_str)
page = Page_Parse(json_str)
page.parse('json')
print("total page : {}".format(page.total_page))
#



#p_parse = Page_Parse(page_data)
#p_parse.parse()





