
"""调度器模块"""
from six.moves.queue import Queue

class Scheduler():

    def __init__(self):
        self.q = Queue()


    def add_request(self,request):
        # 把一个request加入队列中
        self.q.put(request)


    def get_request(self):
        # 从队列中取出一个request对象并返回
        request = self.q.get()
        return request


    def _filter_request(self):
        '''请求去重'''
        # 暂时不实现
        pass





