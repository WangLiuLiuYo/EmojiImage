# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve,urljoin,urlparse
import config
from store.store_picture import store_pictures

def collect_in_page(url, path='', start=1):
    # 伪造的请求头
    name=config.PIC_PRIFIX
    try:
        r = requests.get(url, headers=config.header, timeout=config.request_timeout)
    except:
        print('open web page <', url, " > timeout! i will quit.")
        return start
    count = start  # 图片的计数器
    for img in BeautifulSoup(r.text).find_all('img', class_='BDE_Image'):  # 抓取当前页面的jpg格式图片
        try:
            link = img.get('src')
            store_pictures(link)
            print(link, " downloaded.")
        except:
            print('picture <', img, '> error during download.')
        else:
            count += 1
    for a in BeautifulSoup(r.text).find_all('a'):  # 翻页，采用递归的策略
        if a.get_text() == '下一页':
            newurl = urljoin(url, str(a.get('href')))
            print('goto :', newurl)
            return collect_in_page(newurl, path,count)
        elif a.get_text() == '尾页':
            if urlparse(url)['-2'] == str(a.get('href')):
                print('end to last page :', url)
                return count

    print('page :', url, " collect finish! get picture number:",count)

    return count

def enter(keyword,pgn):
    params={
        'ie':'utf-8',
        'kw':keyword,
        'pn':50*pgn,#每页是有50个连接的。
    }
    #kw是关键词，就是在百度贴吧搜索的那个关键词...
    host='https://tieba.baidu.com/f'
    url='https://tieba.baidu.com/'
    r=requests.get(host,params=params)
    r.encoding='utf-8'
    links=[]
    for a in BeautifulSoup(r.text).find_all('a',class_='j_th_tit '):
        links.append(urljoin(url,str(a.get('href'))))
    return links


