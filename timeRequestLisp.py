from datetime import datetime, timedelta

import json

start_time = datetime.strptime("2024-05-28 00:00:00", "%Y-%m-%d %H:%M:%S")
end_time = datetime.strptime("2024-06-02 00:00:00", "%Y-%m-%d %H:%M:%S")
interval = timedelta(minutes=5)

objects = []

current_time = start_time
while current_time < end_time:
    next_time = current_time + interval
    if next_time > end_time:
        next_time = end_time
    objects.append({
        "handlerName": "ReportStoreWarehouseSummaryHandler",
        "queryDsl": f"update_time[Ge]={current_time.strftime('%Y-%m-%d %H:%M:%S')},update_time[Le]={next_time.strftime('%Y-%m-%d %H:%M:%S')}"
    })
    current_time = next_time

print(json.dumps(objects, indent=2))
