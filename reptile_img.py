#!/usr/bin/python
# encoding: utf-8

# 实现一个简单的爬虫，爬取图片
import urllib.request as urllib
import re
from bs4 import BeautifulSoup
import uuid

#处理print输出 中文乱码
def prints(s):
    # s=s.decode("utf-8").encode("gbk")
    print(s)
 
# 根据url获取网页html内容
def get_html(url):
    page = urllib.urlopen(url)
    return page.read()

# 处理详情页并下载
def get_href(html,page):
    bs4=BeautifulSoup(html,'html.parser')
    num=0
    for x in bs4.find_all('div',class_='picblock'):
        href=x.find('a').get('href')
        html=get_html(href)
        src = get_img_url(html)
        num=num+1
        download_jpg(src,page,num)
 
# 从html中解析出所有jpg图片的url
def get_img_url(html):
    bs4=BeautifulSoup(html,'html.parser')
    src=bs4.find('div',class_="imga").find('img').get('src')
    return src
 
# 批量下载图片，保存到C盘zy文件夹
def download_jpg(url,page,num, path='C:/zy/'):
    # 用于给图片命名
    urllib.urlretrieve(url, ''.join([path, '{0}.jpg'.format(str(page)+'_'+str(num))]))
    prints('----正在下载第'+ str(page) + '页-第'+str(num)+'张-----')
 
# 封装：网页下载图片
def Handle(url,page):
    #解析首页地址
    html = get_html(url)
    #获取详情页地址
    get_href(html,page)
    
 
def main():
    url_temp = 'http://sc.chinaz.com/tag_tupian/yazhoumeinv_{}.html'
    for i in range(2,5):  #第一页的地址和后面的地址有区别  直接从第二页开始 
        url=url_temp.format(i)
        Handle(url,i)
 
if __name__ == '__main__':
    main()
