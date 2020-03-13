import requests

params = {
    'name':'geekdigging',
    'age':'18'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'referer': 'https://www.geekdigging.com/'
}

proxies_socket = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}

# resp = requests.get('https://httpbin.org/get', params, headers=headers)
# print(resp.text)
# print(resp.json())
# print(type(resp.text))

# 利用requests库获取资源
# res = requests.get("https://www.baidu.com/img/superlogo_c4d7df0a003d3db9b65e9ef0fe6da1ec.png")
# with open('F:\\baidu_logo.png', 'wb') as f:
#     f.write(res.content)
#     f.close

resp = requests.post('https://httpbin.org/post', data=params, headers=headers)
print(resp.text)

