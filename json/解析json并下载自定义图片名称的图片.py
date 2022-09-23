#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/23/22 16:55
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : 解析json并下载自定义图片名称的图片.py

import json

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
                response = requests.get(photo_url)
                # 获取的文本实际上是图片的二进制文本
                img = response.content
                # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
                # 保存路径
                download_path = '/Users/steven/Downloads/photo/work/%s.jpg' % self.img_name
                with open(download_path, 'wb') as f:
                    f.write(img)
            except Exception as ex:
                print("--------出错继续----")
                pass


path = r"/Users/steven/PycharmProjects/Python/json/data/作品.json"
file = open(path, 'r', encoding='utf-8')

# 解析数据
records = json.load(file)

# records = data["RECORDS"]


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
            image.download()
            index += 1
