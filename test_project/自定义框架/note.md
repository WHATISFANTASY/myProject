###



###web框架
1.自己写socket，自己处理请求(自己写的框架，tornado-->可以用自己的socket，也可以用wsgi的socket)
2.基于wsgi，自己处理请求（django,flask）

1.自定义框架

```python
#py2.7，自己写socket
import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello,Morra!")
    
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 1234))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()
if __name__ =='__main__':
    main()
```



2.wsgi的框架
1.接受请求 
2.预处理请求

```python
#py2.7
from wsgiref.simple_server import make_server


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #根据url的不同返回不同的字符串
    #1.获取url
    # 2.根据url做不同的响应
    print environ
    return '<h1>Hello, web!</h1>'


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()
```


###路由系统

tornado框架包含两部分
1.接收请求，并封装请求（自己写）
2.处理请求（自己写）



Django框架
1.wsgi
2.Django




自定义web框架
```html
#index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>{{name}}</h1>
<h1>{{age}}</h1>
<h1>{{current_time}}</h1>
<h1>index</h1>
<h1>index</h1>

</body>
</html>
```



```python
# python.py
from wsgiref.simple_server import make_server
import time
from jinja2 import Template


def index():
    data = open('html/index.html').read()
    current_time = str(time.time())
    
    # 模板渲染
    template = Template(data)
    result = template.render(name='Morra', age='123', current_time=current_time)
    return result.encode('utf-8')

def morra():
    data = open('html/morra.html').read()
    return data

url_dict = {'/index': index, '/morra': morra}

# WSGI
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    # 路由系统
    request_url = environ['PATH_INFO']
    print request_url

    if request_url in url_dict:
        return url_dict[request_url]()
    else:
        return '404'


if __name__ == '__main__':
    httpd = make_server('', 8002, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()
```




###MVC架构

Models：处理数据库请求
Views：html模板
Controllers：处理请求的函数


###MTV架构

Models：数据库处理相关 --->不变

Views：html模板 --->Templates

Controllers：处理请求(HTTP请求)的函数   --->Views