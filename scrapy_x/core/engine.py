from scrapy_x.core.scheduler import Scheduler
from scrapy_x.core.downloader import Downloader
from scrapy_x.core.pipeline import Pipeline
from scrapy_x.core.spider import Spider

from scrapy_x.http.request import Request

class Engine():

    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()


    def start(self):
        self._start_engine()


    def _start_engine(self):
        """引擎的内部逻辑"""

        # 1. 爬虫模块发出初始请求
        start_request = self.spider.start_requests()

        # 2. 把初始请求添加给调度器
        self.scheduler.add_request(start_request)

        # 3. 从调度器获取请求对象
        request = self.scheduler.get_request()

        # 4. 利用下载器发起请求获取一个响应对象
        response = self.downloader.get_response(request)

        # 5. 利用爬虫的解析响应的方法，处理响应，得到结果
        result = self.spider.parse(response)

        # 6. 判断结果对象
        if isinstance(result,Request):

            # 6.1 如果是请求对象，那么就再交给调度器
            self.scheduler.add_request(result)

            # 6.2 否则，就交给管道处理
            self.pipeline.process_item(result)

