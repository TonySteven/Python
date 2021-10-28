#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/28/21 14:10
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : spilt.py

from translate import Translator


class Match:
    # '规则对象'
    def __init__(self, value, label):
        # code值
        self.value = value
        # 显示值
        self.label = label

    # 手动拼接也不行
    def toJsonString(self):
        aa = '{"value" : "'
        bb = '" ,"label" : "'
        cc = '"}'
        return aa + self.value + bb + self.label + cc


def translateE2C(m):
    # 英语翻译中文
    translator = Translator(to_lang="chinese")
    translation = translator.translate(m)
    return translation


def translateC2E(m):
    # 中文翻译成英文
    translator = Translator(from_lang="chinese", to_lang="english")
    translation = translator.translate(m)
    return translation


def getSpiltedAndTurnObject(u):
    # 根据顿号转成List[String]
    # 遍历List
    resultList = []
    splitList = u.split('、', -1)
    for i, val in enumerate(splitList):
        # print ("序号：%s   值：%s" % (i + 1, val))
        # n = Match(val, translateE2C(val)).toJsonString()
        # j = json.dumps(n)

        # json2dict
        # d = ast.literal_eval(n)
        n = Match(val, translateE2C(val)).__dict__
        # [{'value': 'total', 'label': '合计'}, {'value': 'average', 'label': '平均'}]
        # 单引号全局替换为双银行即可
        resultList.append(n)

    return resultList
    # return json.dumps(resultList)


if __name__ == '__main__':
    a = input("请输入要json格式化的字符：")
    print('\n')
    print(getSpiltedAndTurnObject(a))
