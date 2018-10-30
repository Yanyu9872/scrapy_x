
"""response响应对象"""

class Response():
    def __init__(self, url, body, headers, status_code):

        self.url = url
        self.body = body
        self.headers = headers
        self.status_code = status_code