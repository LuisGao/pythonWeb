import requests

params = {
    'name':'geekdigging',
    'age':'18'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'referer': 'https://www.geekdigging.com/'
}

resp = requests.get('https://httpbin.org/get', params, headers=headers)
print(resp.text)
print(resp.json())
print(type(resp.text))


