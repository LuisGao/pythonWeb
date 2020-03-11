# import urllib.request, urllib.parse
# import json

# url = 'https://httpbin.org/post'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
#     'Content-Type':'application/json;encoding=utf-8',
#     'Host':'geekdigging.com'
# }
# data = {
#     'name':'geekdigging',
#     'hello':'world'
# }

# data = bytes(json.dumps(data), encoding='utf8')
# request = urllib.request.Request(url=url, data=data,headers=headers,method='POST')
# resp=urllib.request.urlopen(request)
# print(resp.read().decode('utf8'))

import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(cookie)

for item in cookie:
    print(item.name + " = " + item.value)

fileName = 'cookies_mozilla.txt'
cookie = http.cookiejar.MozillaCookieJar(fileName)
cookie.load('cookies_mozilla.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf8'))
# cookie.save(ignore_discard=True, ignore_expires=True)
# print('SaveSUccess')