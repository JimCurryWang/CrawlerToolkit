# CrawlerToolkit
CrawlerToolkit provides several tips in scraping  :blush:  
index: `Proxy` `IP` `Python` `Crawler`

##proxy IP Pool

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
