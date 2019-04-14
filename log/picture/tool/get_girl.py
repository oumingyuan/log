#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
from bs4 import BeautifulSoup
import os
import time
import shutil
from log.picture.tool import zip_tool

'''
不要被这个文件名称迷惑，其实也是可以下载其他图片的，不仅仅是 girl
这个工具类是用来获取网页的图片的，其他的事不做，仅仅是获取图片并下载到本地
'''


# 根据url获取网页html内容
# 只涉及页面内容的获取，其他的事情不做
def get_html_content(url):
    try:
        page = requests.get(url, timeout=100)
        print(page.status_code)

        if page.status_code == 200:
            return page.text
        else:
            return ''

            # raise RuntimeError('你好', '没有成功请求到数据')
    except ReadTimeout:
        print('请求时间大于设定值')
    except HTTPError:
        print('http error')
    except RequestException:
        print('请求数据异常，请确认网络畅通')


def get_jpgs_beautiful(html):
    soup = BeautifulSoup(html, "html.parser")
    img_list = soup.find_all('img')
    list_length = len(img_list)
    jpgs_beautiful = []
    for i in range(list_length):
        dictionary = img_list[i].attrs

        if 'src' in dictionary.keys():
            if 'http' in img_list[i].attrs['src']:
                jpgs_beautiful.append(img_list[i].attrs['src'])
        if 'data-original' in dictionary.keys():
            if 'http' in img_list[i].attrs['data-original']:
                jpgs_beautiful.append(img_list[i].attrs['data-original'])

    return jpgs_beautiful

    # 用图片url下载图片并保存成制定文件名


def download_jpg(img_url, file_name):
    # 可自动关闭请求和响应的模块
    from contextlib import closing
    with closing(requests.get(img_url, stream=True)) as resp:
        with open(file_name, 'wb') as f:
            for chunk in resp.iter_content(128):
                f.write(chunk)


# 批量下载图片，默认保存到当前目录下
def batch_download_jpgs(img_urls):
    # 这是之前的逻辑，现在需要一个唯一的文件夹
    path = './picture/PICTURE' + str(int(round(time.time() * 10000000))) + '/'

    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print('目录已存在')

    # 用于给图片命名
    count = 1
    for img_url in img_urls:
        download_jpg(img_url, ''.join([path, '{0}.jpg'.format(count)]))
        print('下载完成第{0}张图片'.format(count))
        count = count + 1

    return path


# 封装：从百度贴吧网页下载图片
def compressed_files(path):
    pass


'''
返回二进制数组
'''


def download(url):
    # 获取网页源码
    html = get_html_content(url)

    # 获取图片列表
    jpg_beautiful = get_jpgs_beautiful(html)

    if len(jpg_beautiful) == 0:
        return None
    else:

        # 批量下载图片
        path = batch_download_jpgs(jpg_beautiful)

        byte_array = zip_tool.create_zip(path, path[:-1])
        shutil.rmtree(path)  # 递归删除文件夹

        return byte_array
