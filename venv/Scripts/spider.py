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
page_data = fd.get_page(r'http://www.sse.com.cn/assortment/stock/list/share/')

p_parse = Page_Parse(page_data)
p_parse.parse()





