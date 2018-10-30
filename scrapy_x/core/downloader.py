import requests # 第三方模块

from scrapy_x.http.response import Response

"""下载器组件"""

class Downloader(object):
    '''根据请求对象(Request)，发起HTTP、HTTPS网络请求，拿到HTTP、HTTPS响应，构建响应对象(Response)并返回'''
    def get_response(self, request):
        '''发起请求获取响应的方法'''
        if request.method.upper() == 'GET':
            resp = requests.get(request.url, headers=request.headers)


        elif request.method.upper() == 'POST':
            resp = requests.post(request.url, data=request.data, headers=request.headers)

        else:
            # 如果方法不是get或者post，抛出一个异常
            raise Exception("不支持的请求方法")

        return Response(url=resp.url,
                        body=resp.content.decode(),
                        headers=resp.headers,
                        status_code=resp.status_code)
