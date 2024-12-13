import time

import requests

# 定义循环参数列表
lmnid_list = ["72350446169545851"]

# API 的 URL 和 headers
url = "https://supply.imugua.cn/api/chain/sc_quotation_apply/backReviewCommitBillZP"
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "cookie": "Hm_lvt_55ec7104d6d3deee4d7a3e22546f5d9e=1728349930",
    "lmnid": "",  # 占位符，会在循环中更新
    "origin": "https://supply.imugua.cn",
    "priority": "u=1, i",
    "referer": "https://supply.imugua.cn/chaindelivery/DirectAllocation",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "source": "1",
    "token": "lmnchain94c715cba97449f79d7905bcf16bd2ec",
    "traceid": "1734070516680",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# 循环调用 API
results = []  # 用于存储 API 返回结果

for lmnid in lmnid_list:
    payload = {
        "company_id": "171316400792240982",
        "shop_id": "171316400792249951",
        "companyId": "171316400792240982",
        "shopId": "171316400792249951",
        "token": "lmnchain94c715cba97449f79d7905bcf16bd2ec",
        "LmnID": lmnid,
        "lmnid": lmnid
    }

    # 更新 header 中的 lmnid
    headers["lmnid"] = lmnid

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # 检查请求是否成功
        result = response.json()
        results.append({"lmnid": lmnid, "response": result})
        print(f"成功调用 API，LmnID: {lmnid}, 响应: {result}")
    except requests.exceptions.RequestException as e:
        print(f"调用 API 出错，LmnID: {lmnid}, 错误: {e}")

    # 避免频繁调用，可设置延时
    time.sleep(1)  # 延时 1 秒

# 打印所有结果
print("所有结果:")
for item in results:
    print(item)

# 保存结果到文件（可选）
with open("api_results.json", "w", encoding="utf-8") as f:
    import json

    json.dump(results, f, ensure_ascii=False, indent=4)
