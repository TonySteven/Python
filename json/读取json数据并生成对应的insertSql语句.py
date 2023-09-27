#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 6/10/22 16:24
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : 读取Excel数据并转换成json.py

import json
import uuid


def convert_to_lowercase_if_all_uppercase(input_str):
    # 判断字符串是否全部为大写
    if input_str.isupper():
        # 如果是大写，则转换为小写
        return input_str.lower()
    else:
        return input_str  # 如果不是大写，返回原始字符串


def remove_trailing_zeros(input_str):
    # 将输入字符串转换为浮点数，然后再转换回字符串
    cleaned_str = str(float(input_str))
    return cleaned_str


def generate_unique_id():
    unique_id = str(uuid.uuid4().int)[:19]  # 获取 UUID 的整数表示并截取前 19 位
    return unique_id


def create_insert_sql_save(open_path, save_path):
    """
    生成insert sql语句并保存到本地
    :param open_path:
    :param save_path:
    :return:
    """

    # 加载文件
    file_read = open(open_path, 'r', encoding='utf-8')
    file_out = open(save_path, 'a')

    # 读取文件
    records = json.load(file_read)
    for record in records:
        # 雪花算法生成19位数字id字段
        lmnid = str(generate_unique_id())
        # 获取lmnid
        dish_code = str(record['lmnid'])
        # 获取货号并转换成str + 00001
        item_number = record['货号']
        item_number = str(item_number) + "00001"
        # 获取名称
        name = str(record['名称'])
        # 获取规格
        standard = str(record['规格'])
        # 获取单位
        unit = convert_to_lowercase_if_all_uppercase(str(record['新增单位']))
        # 获取 新增单位转换率
        rate_of_def = remove_trailing_zeros(str(record['新增单位转换率']))

        # 根据INSERT INTO gyl_def.sc_dish_unit (company_id, shop_id, status_, lmnid, name, dish, dish_code,
        #                                   Rate_of_def, Item_number, Purchase_unit, Distribution_unit, Standard,
        #                                   Check_unit)
        # VALUES ('1634800674453000010', '1634800674465000030', 1, '7975217088582549505', 'kg', '安佳奶油乳酪（5KG*4包）',
        #         '7530810809468934846', '12000', '600302', 0, 0, '12kg', 1);
        # 生成insert sql语句,拼接values 后面的值
        # inset_sql = ("INSERT INTO gyl_def.sc_dish_unit (company_id, shop_id, status_, lmnid, name, dish, dish_code, " +
        #              "Rate_of_def, Item_number, Purchase_unit, Distribution_unit, Standard, Check_unit) VALUES (" +
        #              "'1634800674453000010', '1634800674465000030', 1, '" + lmnid + "', ' " + unit + "', '" + name + "', '"
        #              + dish_code + "', '" + rate_of_def + "' , '" + item_number + "', 0, 0,'" + standard + "', 1);")

        inset_sql = ("INSERT INTO gyl_def.sc_dish_unit (company_id, shop_id, status_, lmnid, name, dish"
                     ", dish_code,Rate_of_def, Item_number, Purchase_unit, Distribution_unit, Standard,Check_unit)"
                     "VALUES "
                     "('1634800674453000010', '1634800674465000030', 1, '{lmnid}', '{unit}', '{name}', '{dish_code}',"
                     " '{rate_of_def}', '{item_number}', 0, 0, '{standard}', 1);").format(lmnid=lmnid, unit=unit,
                                                                                          name=name,
                                                                                          dish_code=dish_code,
                                                                                          rate_of_def=rate_of_def,
                                                                                          item_number=item_number,
                                                                                          standard=standard)

        file_out.write(inset_sql)
        file_out.write("\n")


if __name__ == '__main__':
    open_path = r'./book/transform.json'
    save_path = './book/insert.sql'
    create_insert_sql_save(open_path, save_path)
