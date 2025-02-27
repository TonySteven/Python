import os

import pandas as pd
import requests

import json

# 常量配置
TOKEN = 'lmnchain4a0e97068d524063933871329f69599c'  # 请替换为实际的 token
API_URL = 'https://supply.umugua.net/api-v2/scm-base-data/car-driver-binding/add'
COMPANY_ID = "1645512743732000029"
BRAND_ID = "1645512743763000017"


# 读取 JSON 数据文件
def load_json_file(file_path):
    """加载并返回 JSON 数据"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"错误：文件未找到 {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"错误：JSON 格式错误 {file_path}")
        return []


# 读取 Excel 数据文件
def load_excel_file(file_path):
    """读取 Excel 文件并返回 DataFrame"""
    if not os.path.exists(file_path):
        print(f"错误：文件未找到 {file_path}")
        return pd.DataFrame()
    return pd.read_excel(file_path, sheet_name='Sheet1')


# 生成映射字典（车牌号 -> lmnid，姓名 -> lmnid）
def create_mapping(data, key_field, value_field):
    """创建映射字典，从数据中提取车牌号或姓名和对应的 lmnid"""
    mapping = {}

    # 遍历数据并构建映射
    for entry in data:
        try:
            # 获取字段值，并清理空格
            key = entry.get(key_field)
            value = entry.get(value_field)

            # 调试输出：打印 key 和 value 确认其值
            if not key:
                print(f"警告：数据条目 {entry} 的 {key_field} 字段为空或无效")

            if not value:
                print(f"警告：数据条目 {entry} 的 {value_field} 字段为空或无效")

            # 如果 key 和 value 都有效，才加入映射
            if key and value:
                mapping[key] = value
            else:
                print(f"警告：数据条目 {entry} 的 {key_field} 或 {value_field} 缺失或无效")

        except KeyError as e:
            print(f"警告：数据条目缺少关键字段 {str(e)}")

    return mapping


# 发送 POST 请求
def send_post_request(payload):
    """发送 POST 请求到 API"""
    headers = {
        'accept': 'application/json',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://supply.umugua.net',
        'referer': 'https://supply.umugua.net/businessprofiles/distributionbusiness/DistributionCarInfo',
        'token': TOKEN,  # 使用全局变量
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # 如果响应码不是2xx，抛出异常
        return response
    except requests.exceptions.RequestException as e:
        print(f"错误：API 请求失败: {e}")
        return None


# 主流程
def main():
    # 文件路径
    car_file_path = '/Users/steven/PycharmProjects/Python/bty/json/car.json'
    driver_file_path = '/Users/steven/PycharmProjects/Python/bty/json/driver.json'
    excel_file_path = '/Users/steven/Downloads/副本司机电话.xlsx'

    # 加载车牌号和司机数据
    car_data = load_json_file(car_file_path)
    driver_data = load_json_file(driver_file_path)

    if not car_data or not driver_data:
        print("错误：车牌号或司机数据加载失败")
        return

    # 创建车牌号和司机的映射字典
    car_map = create_mapping(car_data, 'car_no', 'lmnid')
    driver_map = create_mapping(driver_data, 'name', 'lmnid')

    # 读取 Excel 数据
    sheet_data = load_excel_file(excel_file_path)
    if sheet_data.empty:
        return

    # 清理数据
    sheet_data.columns = ['Name', 'License Plate', 'Phone']
    sheet_data = sheet_data.drop(index=0)  # 移除第一行（通常是表头）

    # 遍历司机数据并调用 API
    for index, row in sheet_data.iterrows():
        name = row['Name'].strip().replace(" ", "")  # 去掉姓名中的空格
        license_plate = row['License Plate'].strip().replace(" ", "")  # 去掉车牌号中的空格

        # 获取车牌号和司机姓名对应的 lmnid
        car_id = car_map.get(license_plate)
        driver_id = driver_map.get(name)

        # 如果车牌号和司机都能找到对应的 lmnid，则构造请求
        if car_id and driver_id:
            payload = {
                "company_id": COMPANY_ID,
                "companyId": COMPANY_ID,
                "brandId": BRAND_ID,
                "token": TOKEN,
                "carId": str(car_id),
                "driverDataList": [{
                    "driverId": str(driver_id),
                    "isMainDriver": 1  # 默认设置为主驾驶员
                }]
            }

            # 发送 POST 请求
            response = send_post_request(payload)
            if response:
                print(f"API 调用 车牌号 {license_plate} 与 司机 {name} (车ID: {car_id}, 司机ID: {driver_id}) - "
                      f"状态: {response.status_code}, 响应: {response.text}")
        else:
            print(f"警告：车牌号 {license_plate} 或 司机 {name} 的映射信息丢失！")


if __name__ == '__main__':
    main()
