
'''爬虫组件封装'''

from scrapy_x.http.request import Request
from scrapy_x.item import Item

"""爬虫模块"""

class Spider():

    start_url = 'http://www.itcast.cn' # 临时写死

    def start_requests(self):
        # 构造起始url为request并返回
        return Request(self.start_url)


    def parse(self, response):
        # 解析函数,并返回新的请求对象、或者数据对象
        return Item(response.body)