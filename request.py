import requests
import time
from lxml import etree
import xlwt

# test AuthorName

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

# resp = requests.post('https://httpbin.org/post', data=params, headers=headers)
# print(resp.text)
# print(resp.cookies)

headers = {
    'host':'xa.ke.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/74.0'
}

TITLES = []
PRICES = []

def getListPage(url):
    resp = requests.get(url)
    doc = resp.content.decode('utf-8')
    # print(resp.content.decode('utf-8'))

    # get response body
    html = etree.HTML(doc)
    # get folder list
    title_list = html.xpath('/html/body/div[1]/div[5]/div[1]/div[4]/ul/li/div[1]/div[1]/a/text()')
    price_list = html.xpath('/html/body/div[1]/div[5]/div[1]/div[4]/ul/li/div[1]/div[2]/div[@class="totalPrice"]/span/text()')

    for i in range(len(title_list)):
        TITLES.append(title_list[i])
        PRICES.append(price_list[i])

    print(len(title_list))
    if len(title_list) > 0:
        print('page: ' + url + ' get Success!')
    else:
        print('page: ' + url + ' get Error!')

    # get link list
    # price_list = html.xpath('//*[@id="pins"]/li/a/@href')

def writeToExcel():
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    for i in range(len(TITLES)):
        sheet1.write(i, 0, TITLES[i])
        sheet1.write(i, 1, PRICES[i])
    workbook.save('F:\\北京二手房交易记录.xls')
    print('二手房数据保存完毕')

def main():

    getListPage('https://bj.ke.com/chengjiao/')
    for i in range(100):
        if i == 0:
            continue
        time.sleep(3)
        getListPage('https://bj.ke.com/chengjiao/pg' + str(i + 1) + '/')    
    writeToExcel()

if __name__ == '__main__':
    TITLES = ['基本信息']
    PRICES = ['成交价格']
    # writeToExcel()
    main()

# r = requests.get('https://xa.ke.com/chengjiao/pg100/')
# print(r.content)
