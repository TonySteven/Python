import requests

import json

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
    'token': 'lmnchain01155e935fca420ea0bb3716cac2375c',  # 替换为你自己的 token
    'traceid': '1740534489573',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

# 车牌号列表
car_numbers = [
    "鲁AJ95F6", "鲁A77M8U", "鲁U3C109", "鲁J880ⅤY", "鲁AFR6176", "鲁AFQ0777", "鲁A39Q2L",
    "鲁USM156", "鲁A7F3K9", "鲁BY396W", "鲁USJ809", "鲁FR96Q9", "鲁KP6S10", "鲁BYP015",
    "鲁A28U5V", "鲁U3E701", "鲁U15Z31", "鲁BL3965", "鲁UJS092", "鲁U9B698", "鲁B0Q6S6",
    "鲁UKB367", "鲁U9E352", "鲁B56T2F", "鲁BF731B", "鲁B593X3", "鲁UMC355", "鲁UHG527",
    "鲁B93RB6", "鲁B9G673", "鲁BCB575", "鲁UWS139", "鲁B7Y660", "鲁G0E88E", "鲁A39Q2L",
    "鲁U6D613", "鲁B06J63", "鲁UN3350", "鲁BL5835"
]

# 循环遍历车牌号列表并调用 API
for car_number in car_numbers:
    payload = {
        "company_id": "1645512743732000029",
        "shop_id": "1645512743763000017",
        "companyId": "1645512743732000029",
        "shopId": "1645512743763000017",
        "token": "lmnchain01155e935fca420ea0bb3716cac2375c",  # 替换为你自己的 token
        "car_no": car_number,
        "brand": "半天妖"  # 车品牌
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # 输出每次 API 调用的响应状态和信息
    print(f"API 调用 车牌号 {car_number}: {response.status_code}, {response.text}")
