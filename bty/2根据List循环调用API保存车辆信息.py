import os

import pandas as pd
import requests

import json

# 定义常量 token
TOKEN = 'lmnchain4a0e97068d524063933871329f69599c'

# 读取上传的 Excel 文件
file_path = r'/Users/steven/Downloads/副本司机电话.xlsx'
if not os.path.exists(file_path):
    print(f"文件不存在: {file_path}")
else:
    print(f"文件路径存在: {file_path}")

sheet_data = pd.read_excel(file_path, sheet_name='Sheet1')

# 清理数据
sheet_data.columns = ['Name', 'License', 'Phone']
sheet_data = sheet_data.drop(index=0)

# API URL
url = 'https://supply.umugua.net/api/chain/scCar/save'

# 设置请求头
headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'dnt': '1',
    'origin': 'https://supply.umugua.net',
    'priority': 'u=1, i',
    'referer': 'https://supply.umugua.net/businessprofiles/distributionbusiness/DistributionCarInfo',
    'sec-ch-ua': '"Chromium";v="133", "Not(A:Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'source': '1',
    'token': TOKEN,  # 使用全局变量
    'traceid': '1740534489573',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

# 循环遍历车牌号列表并调用 API
for index, row in sheet_data.iterrows():
    # 清理 License 列，移除所有空格
    car_number = row['License'].strip().replace(" ", "")

    # 如果车牌号为空，则跳过该行
    if not car_number:
        print(f"跳过空车牌号，第 {index + 1} 行")
        continue

    payload = {
        "company_id": "1645512743732000029",
        "shop_id": "1645512743763000017",
        "companyId": "1645512743732000029",
        "shopId": "1645512743763000017",
        "token": TOKEN,  # 使用全局变量
        "car_no": car_number,
        "brand": "半天妖"  # 车品牌
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # 输出每次 API 调用的响应状态和信息
    print(f"API 调用 车牌号 {car_number}: {response.status_code}, {response.text}")