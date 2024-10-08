from datetime import datetime, timedelta

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

print(json.dumps(requestBodyList, indent=2))
