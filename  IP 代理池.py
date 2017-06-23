
'''
#對於限制訪問速度的情況，我們可以通過time.sleep進行短暫休眠後再次爬取。
#對於限制ip訪問次數的時候我們需要通過代理ip輪換去訪問目標網址。

免費代理ip的網址: url = 'http://www.xicidaili.com/nn/'

第一步：構造請求代理ip網站鏈接      => def get_url(url):
第二步：獲取網頁內容               => def get_content(url):
第三步：提取網頁中ip地址和端口號信息 => def get_info(content):
第四步：驗證代理ip的有效性          => def verif_ip(ip,port): 
最後：調用各個函數
'''

import urllib.request
import time
from lxml import etree

def get_url(url):    # 高匿代理鏈接 from China
    url_list = []
    for i in range(1,100):
        url_new = url + str(i)
        url_list.append(url_new)
    return url_list

def get_content(url):    # 獲取網頁內容
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    content = res.read()
    return content.decode('utf-8')


def get_info(content):      # 提取網頁信息 / ip 端口
    datas_ip = etree.HTML(content).xpath('//table[contains(@id,"ip_list")]/tr/td[2]/text()')
    datas_port = etree.HTML(content).xpath('//table[contains(@id,"ip_list")]/tr/td[3]/text()')
    with open("data.txt", "w") as fd:
        for i in range(0,len(datas_ip)):
            out = u""
            out += u"" + datas_ip[i]
            out += u":" + datas_port[i]
            fd.write(out + u"\n")    # 所有ip和端口號寫入data文件

def verif_ip(ip,port):    # 驗證ip有效性
    user_agent ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent':user_agent}
    proxy = {'http':'http://%s:%s'%(ip,port)}
    print(proxy)

    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    test_url = "https://www.baidu.com/"
    req = urllib.request.Request(url=test_url,headers=headers)
    time.sleep(6)
    try:
        res = urllib.request.urlopen(req)
        time.sleep(3)
        content = res.read()
        if content:
            print('that is ok')
            with open("data2.txt", "a") as fd:      # 有效ip保存到data2文件夾
                fd.write(ip + u":" + port)
                fd.write("\n")
        else:
            print('its not ok')
    except urllib.request.URLError as e:
        print(e.reason)


if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    url_list = get_url(url)
    for i in url_list:
        print(i)
        content = get_content(i)
        time.sleep(3)
        get_info(content)

    with open("dali.txt", "r") as fd:
        datas = fd.readlines()
        for data in datas:
            print(data.split(u":")[0])
        # print('%d : %d'%(out[0],out[1]))
            verif_ip(data.split(u":")[0],data.split(u":")[1])