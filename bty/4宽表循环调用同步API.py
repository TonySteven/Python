import datetime

import requests

# 配置项
TYPE = "TPRKD"
COMPANY_ID = "166640201824483138"
SHOP_ID = "166640201824425866"
TOKEN = "lmnchaindc3dc81156be4adf89e5f7784e7706e9"
USER_AGENT = "Apifox/1.0.0 (https://apifox.com)"
URL = "https://pre-supply.imugua.team/api/chain/sync/scmBill"

# 日期范围配置
start_date = datetime.date(2025, 2, 1)
end_date = datetime.date(2025, 2, 28)

# 步长设置
step = datetime.timedelta(days=1)

# 循环日期范围，步长为1天
current_date = start_date
while current_date < end_date:
    # 构造 beginBusinessDate 和 endBusinessDate
    begin_business_date = current_date.strftime("%Y-%m-%d")
    end_business_date = (current_date + step).strftime("%Y-%m-%d")

    # 请求数据
    payload = {
        "beginBusinessDate": begin_business_date,
        "endBusinessDate": end_business_date,
        "type": TYPE,
        "companyId": COMPANY_ID,
        "shopId": SHOP_ID
    }

    headers = {
        "token": TOKEN,
        "User-Agent": USER_AGENT,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Host": "pre-supply.imugua.team",
        "Connection": "keep-alive"
    }

    response = requests.post(URL, json=payload, headers=headers)

    # 打印返回的结果
    if response.status_code == 200:
        print(f"成功请求 {begin_business_date} 到 {end_business_date}")
    else:
        print(f"请求失败 {begin_business_date} 到 {end_business_date}: {response.status_code}, {response.text}")

    # 更新日期
    current_date += step
