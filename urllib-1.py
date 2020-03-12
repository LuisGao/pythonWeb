import urllib.request
import urllib.parse
import socket

# urllib简单尝试

try:
    post_data = bytes(urllib.parse.urlencode({'name':'geekdigging', 'hello':'world'}), encoding='utf8')
    response = urllib.request.urlopen('https://httpbin.org/post', data=post_data,timeout=0.1)
    print(response.read().decode('utf8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('请求超时')
    else:
        print(e) 