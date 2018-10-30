
"""request请求对象"""

class Request():

    def __init__(self, url, method='GET', data=None, headers=None):

        self.url = url
        self.method = method
        self.data = data
        self.headers = headers