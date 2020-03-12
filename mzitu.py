import urllib.request, urllib.parse
from lxml import etree
import time

# Build Request Header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'referer' : 'https://www.mzitu.com/'
}

# Save path
save_path = 'F:\\MZiTu'

import os

# 创建文件夹
def creatFile(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    os.chdir(file_path)

# 爬取数据
def get_outer(outer_url):
    req = urllib.request.Request(url=outer_url, headers=headers, method = "GET")
    resp = urllib.request.urlopen(req)
    # get response body
    html = etree.HTML(resp.read().decode('utf-8'))
    # get folder list
    title_list = html.xpath('//*[@id="pins"]/li/a/img/@alt')
    # get link list
    src_list = html.xpath('//*[@id="pins"]/li/a/@href')

    print('当前页面' + outer_url + ', 共计爬取' + str(len(title_list)) + '个文件夹')

    for i in range(len(title_list)):
        file_path = save_path + '\\' + title_list[i]
        img_url = src_list[i]
        creatFile(file_path)
        get_inner(img_url, file_path)

def get_inner(url, file_path):
    req = urllib.request.Request(url = url, headers=headers, method='GET')
    resp = urllib.request.urlopen(req)

    html = etree.HTML(resp.read().decode('utf-8'))
    # get max pageNumber
    max_num = html.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()')[0]
    print('当前页面url：', url, ', 最大页数为', max_num)

    for i in range(1, int(max_num)):
        time.sleep(1)

        inner_url = url + '/' + str(i)
        inner_req = urllib.request.Request(url=inner_url, headers=headers,method='GET')
        inner_resp = urllib.request.urlopen(inner_req)

        inner_html = etree.HTML(inner_resp.read().decode('utf-8'))
        img_src = inner_html.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')[0]
        file_name = str(img_src).split('/')[-1]

        # download picture
        try:
            request = urllib.request.Request(url=img_src, headers=headers, method='GET')
            img_resp = urllib.request.urlopen(request)
            get_img = img_resp.read()

            file_os_path = file_path + '\\' + file_name
            if os.path.isfile(file_os_path):
                print('图片已经存在: ', file_os_path)
                pass
            else:
                with open(file_os_path, 'wb') as fp:
                    fp.write(get_img)
                    print('图片保存：' , file_os_path)
                    fp.close()
        except Exception as e:
            print('图片拉取失败')

def main():
    url = 'https://www.mzitu.com/xinggan/page/'
    for i in range(1, 168):
        get_outer(url + str(i))

if __name__ == '__main__':
    # main()
    url = 'https://www.mzitu.com/xinggan/page/'
    for i in range(1, 168):
        get_outer(url + str(i))


# 笔记：
# 1. urllib三部曲得到body
# 2. 从body利用规则的布局，根据正则表达式得到内容
# 3. 可以通过获取href的方法得到跳转
# 4. 保存img的方法：fp直接存image文件即可
