from datetime import datetime, timedelta

import requests

import json

start_time = datetime.strptime("2024-05-01 00:00:00", "%Y-%m-%d %H:%M:%S")
end_time = datetime.strptime("2024-06-01 00:00:00", "%Y-%m-%d %H:%M:%S")
interval = timedelta(minutes=180)

requestBodyList = []

current_time = start_time
while current_time < end_time:
    next_time = current_time + interval
    if next_time > end_time:
        next_time = end_time
    requestBodyList.append({
        "handlerName": "ReportStoreWarehouseSummaryHandler",
        "queryDsl": f"update_time[Ge]={current_time.strftime('%Y-%m-%d %H:%M:%S')},update_time[Le]={next_time.strftime('%Y-%m-%d %H:%M:%S')},company_id[Eq]=1634800674453000010"
    })
    current_time = next_time

# 请求的 URL
url = 'https://extract.imugua.cn/timings-full'

# 请求头
headers = {
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Host': 'extract.imugua.cn',
    'Connection': 'keep-alive'
}

# 遍历列表并发送 POST 请求
for data in requestBodyList:
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 输出响应结果
    print(f"Request Data: {data}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}\n")
