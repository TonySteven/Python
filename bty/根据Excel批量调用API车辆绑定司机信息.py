import os

import pandas as pd
import requests

import json

# 读取 car.json 和 driver.json 文件
with open('/Users/steven/PycharmProjects/Python/bty/json/car.json', 'r', encoding='utf-8') as car_file:
    car_data = json.load(car_file)

with open('/Users/steven/PycharmProjects/Python/bty/json/driver.json', 'r', encoding='utf-8') as driver_file:
    driver_data = json.load(driver_file)

# 将车牌号映射到 lmnid
car_map = {car['car_no']: car['lmnid'] for car in car_data}

# 将司机姓名映射到 lmnid
driver_map = {driver['name']: driver['lmnid'] for driver in driver_data}

# 读取上传的 Excel 文件
file_path = r'/Users/steven/Downloads/司机电话(1).xlsx'
if not os.path.exists(file_path):
    print(f"文件不存在: {file_path}")
else:
    print(f"文件路径存在: {file_path}")

sheet_data = pd.read_excel(file_path, sheet_name='Sheet1')

# 清理数据
sheet_data.columns = ['Name', 'License Plate', 'Phone']
sheet_data = sheet_data.drop(index=0)

# API URL
url = 'https://supply.umugua.net/api-v2/scm-base-data/car-driver-binding/add'

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
    'token': 'lmnchain01155e935fca420ea0bb3716cac2375c',  # 替换为你自己的 token
    'traceid': '1740535057245',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

# 循环遍历司机表格数据，根据车牌号和姓名找到对应的 lmnid 并调用 API
for index, row in sheet_data.iterrows():
    name = row['Name']
    license_plate = row['License Plate']

    # 获取车牌号和司机姓名对应的 lmnid
    car_id = car_map.get(license_plate)
    driver_id = driver_map.get(name)

    if car_id and driver_id:
        # 构造请求 payload
        payload = {
            "company_id": "1645512743732000029",
            "companyId": "1645512743732000029",
            "brandId": "1645512743763000017",
            "token": "lmnchain01155e935fca420ea0bb3716cac2375c",  # 替换为你自己的 token
            "carId": str(car_id),
            "driverDataList": [{
                "driverId": str(driver_id),
                "isMainDriver": 1
            }]
        }

        # 发送 POST 请求
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # 输出每次 API 调用的响应状态和信息
        print(
            f"API 调用 车牌号 {license_plate} 与 司机 {name} (车ID: {car_id}, 司机ID: {driver_id}): {response.status_code}, {response.text}")
    else:
        print(f"车牌号 {license_plate} 或 司机 {name} 的映射信息丢失！")
