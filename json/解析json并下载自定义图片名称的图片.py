#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/23/22 16:55
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : 解析json并下载自定义图片名称的图片.py

import datetime
import json
# from fake_useragent import UserAgent
from multiprocessing.dummy import Pool as ThreadPool

import requests


class DownloadImage:
    def __init__(self, download_url, image_name, **kw):
        self.download_url = download_url
        self.img_name = image_name
        for k, v in kw.items():
            setattr(self, k, v)

    def download(self):
        if self.download_url:
            download_name = self.img_name + '.jpg'
            print("-----------正在下载图片 %s" % download_name)
            try:
                photo_url = self.download_url
                # headers = {'User-Agent': UserAgent().random}
                response = requests.get(url=photo_url, timeout=8)
                # 获取的文本实际上是图片的二进制文本
                img = response.content
                # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
                # 保存路径
                download_path = '/Users/steven/Downloads/photo/work/%s.jpg' % self.img_name
                with open(download_path, 'wb') as f:
                    f.write(img)
            except Exception as ex:
                print("------出错继续----")
                pass

    # 多线程下载图片数据
    def thread_down(self, num_processes=4, Async=True):

        try:
            # 开4个 worker，没有参数时默认是 cpu 的核心数
            pool = ThreadPool(processes=num_processes)
            if Async:
                pool.apply_async(func=self.download)
            else:
                pool.apply(func=self.download)
            pool.close()
            pool.join()
            download_name = self.img_name + '.jpg'
            print("-----------下载图片: %s 成功!" % download_name)
        except Exception as ex:
            # print("Error: unable to start thread")
            print("-----报错-------" + str(ex))
            pass


path = r"/Users/steven/PycharmProjects/Python/json/data/作品.json"
file = open(path, 'r', encoding='utf-8')

# 解析数据
records = json.load(file)
# records = data["RECORDS"]

# 记录开始时间
access_start = datetime.datetime.now()
access_start_str = access_start.strftime('%Y-%m-%d %H:%M:%S')
print("开始时间: %s" % access_start_str)

for record in records:
    nickname = record["nickname"]
    title = record["title"]
    img_info = record["img"]

    if img_info != '':
        img_info_lists = json.loads(img_info)
        index = 0
        for img_info_list in img_info_lists:
            url = img_info_list["url"]
            img_name = nickname + '_' + title + '_' + str(index)
            image = DownloadImage(url, img_name)
            # 下载图片
            # image.download()
            # 多线程下载图片
            image.thread_down(4, False)
            index += 1

# 记录结束时间
access_end = datetime.datetime.now()
access_end_str = access_end.strftime('%Y-%m-%d %H:%M:%S')
print("结束时间: %s" % access_end_str)
access_delta = (access_end - access_start).seconds * 1000
print("------总时长(毫秒)----" + str(access_delta))
