import os

import pandas as pd
import requests

import json

# 定义常量 token
TOKEN = 'lmnchainf8d521edecb54af3ad5baaaeda345e83'  # 替换为你自己的 token

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
url = 'https://supply.umugua.net/api/chain/scDriver/save'

# 设置请求头
headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'dnt': '1',
    'origin': 'https://supply.umugua.net',
    'priority': 'u=1, i',
    'referer': 'https://supply.umugua.net/businessprofiles/distributionbusiness/DistributionDriverInfo',
    'sec-ch-ua': '"Chromium";v="133", "Not(A:Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'source': '1',
    'token': TOKEN,  # 使用常量 token
    'traceid': '1740533349047',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

# 循环遍历数据并调用 API
for index, row in sheet_data.iterrows():
    # 清理 Name 和 Phone 列，移除多余的空格
    name = row['Name'].strip()
    phone = row['Phone'].strip()

    # 如果 Name 或 Phone 为空，则跳过该行
    if not name or not phone:
        print(f"跳过数据，第 {index + 1} 行，缺少 Name 或 Phone")
        continue

    payload = {
        "company_id": "1645512743732000029",
        "shop_id": "1645512743763000017",
        "companyId": "1645512743732000029",
        "shopId": "1645512743763000017",
        "token": TOKEN,  # 使用常量 token
        "name": name,
        "Phone": phone,
        "id_number": ""  # 这里可以放置一个 id_number
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # 输出每次 API 调用的响应状态和信息
    print(f"API 调用 {name} - {phone}: {response.status_code}, {response.text}")
