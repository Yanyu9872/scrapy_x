from _datetime import datetime

from scrapy_x.core.scheduler import Scheduler
from scrapy_x.core.downloader import Downloader
from scrapy_x.core.pipeline import Pipeline
from scrapy_x.core.spider import Spider

from scrapy_x.http.request import Request

from scrapy_x.middlewares.spider_middlewares import SpiderMiddleware
from scrapy_x.middlewares.downloader_middlewares import DownloaderMiddleware
from scrapy_x.utils.log import logger


class Engine():
    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

        self.spider_mid = SpiderMiddleware()  # 初始化爬虫中间件对象
        self.downloader_mid = DownloaderMiddleware()  # 初始化下载器中间件对象

    def start(self):
        '''程序入口'''
        start = datetime.now()  # 起始时间
        logger.info("开始运行时间：%s" % start)  # 使用日志记录起始运行时间
        self._start_engine()
        stop = datetime.now()  # 结束时间
        logger.info("开始运行时间：%s" % stop)  # 使用日志记录结束运行时间
        logger.info("耗时：%.2f" % (stop - start).total_seconds())  # 使用日志记录运行耗时


    def _start_engine(self):
        """引擎的内部逻辑"""

        # 1. 爬虫模块发出初始请求
        start_request = self.spider.start_requests()

        # 利用爬虫中间件预处理请求对象
        start_request =self.spider_mid.process_request(start_request)

        # 2. 把初始请求添加给调度器
        self.scheduler.add_request(start_request)

        # 3. 从调度器获取请求对象
        request = self.scheduler.get_request()

        # 利用下载器中间件预处理请求对象
        request = self.downloader_mid.process_request(request)

        # 4. 利用下载器发起请求获取一个响应对象
        response = self.downloader.get_response(request)

        # 利用下载器中间件预处理响应对象
        response = self.downloader_mid.process_response(response)

        # 利用爬虫中间件预处理响应对象
        response = self.spider_mid.process_response(response)

        # 5. 利用爬虫的解析响应的方法，处理响应，得到结果
        result = self.spider.parse(response)

        # 6. 判断结果对象
        if isinstance(result, Request):

            # 利用爬虫中间件预处理请求对象
            result = self.spider_mid.process_request(result)

            # 6.1 如果是请求对象，那么就再交给调度器
            self.scheduler.add_request(result)
        else:
            # 6.2 否则，就交给管道处理
            self.pipeline.process_item(result)
