# URL解析的模块：提供一套解析URL的方法，提取关键属性和获得数据字段

# https://www.geekdigging.com/2019/12/05/104488944/

from urllib.parse import urlparse, urlunparse

result = urlparse('https://docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse')
print(type(result))
print(result)

params = ('https', 'www.geekdigging.com', 'index.html', 'people', 'a=1', 'geekdigging')
print(urlunparse(params))

from urllib.parse import urlsplit, urlunsplit

result_urlsplit = urlsplit("https://www.geekdigging.com/index.html;people?a=1#geekdigging")
print(type(result_urlsplit))
print(result_urlsplit)

params_urlunsplit = ('https', 'www.geekdigging.com', 'index.html;people', 'a=1', 'geekdigging')
print(urlunsplit(params_urlunsplit))

from urllib.parse import urlencode
# urlencode 示例
dict = {
    "name": "极客挖掘机",
    "age": 18
}
print("https://www.geekdigging.com/" + urlencode(dict))
