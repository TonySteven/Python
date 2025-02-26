import json
from datetime import datetime, timedelta

import requests

start_time = datetime.strptime("2025-02-01 00:00:00", "%Y-%m-%d %H:%M:%S")
end_time = datetime.strptime("2025-02-24 00:00:00", "%Y-%m-%d %H:%M:%S")

interval = timedelta(minutes=5)
# 按照一个月步长同步
# interval = timedelta(days=10)

requestBodyList = []

current_time = start_time
while current_time < end_time:
    next_time = current_time + interval
    if next_time > end_time:
        next_time = end_time
    requestBodyList.append({
        "handlerName": "ReportTertiaryAccountCopyHandler",
        "queryDsl": f"update_time[Ge]={current_time.strftime('%Y-%m-%d %H:%M:%S')},update_time[Le]={next_time.strftime('%Y-%m-%d %H:%M:%S')},company_id[Eq]=1645512743732000029"
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

# 初始化任务id list
task_id_list = []

# 遍历列表并发送 POST 请求
for data in requestBodyList:
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 输出响应结果
    print(f"Request Data: {data}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}\n")
    # response.id set 到task_id_list中
    task_id_list.append(response.json().get('id'))

# 最后控制台 打印 task_id_list
print(f"task_id_list: {task_id_list}")
