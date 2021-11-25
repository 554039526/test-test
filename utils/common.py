# -*- coding: utf-8 -*-
"""
    @File: common.py
    @Desc: 常用业务工具
    @Time: 2021/11/18 10:56 下午
    @Author: Wan Wenlong
"""
import re
from mimesis import Person, Business
from mimesis.enums import Gender
from mimesis.schema import Schema
import random

phone = ['13900000000', '13900000001']
p = Person('zh')
b = Business('zh')


def get_phone(business, unique=True, i=1):
    """
    生成对应业务的手机号
    :param business: 业务
    :param unique: 是否唯一
    :return:
    """

    # res = p.telephone(mask='13#########')
    phone_tel = '1390000000' + str(i)
    if unique:
        if phone_tel in phone:
            i += 1
            return get_phone(business, unique=True, i=i)
        else:
            print(phone_tel)
            return phone_tel
    else:
        return phone_tel


print(get_phone(1, unique=True, i=1))


def get_person_name(sex='Female'):
    """
    返回人的姓名
    :param sex:
    :return:
    """
    if sex == 'Female':
        name = p.surname(Gender.FEMALE) + p.name(Gender.FEMALE)
    else:
        name = p.surname(Gender.MALE) + p.name(Gender.MALE)
    return name


# print(get_person_name())
company = ['集团1', '集团2']


def get_company_name(unique=False, i=1):
    """
    返回公司的名称
    :return:
    """
    # res = b.company() + b.company_type()
    res = '集团' + str(i)
    if unique:
        if res in company:
            i += 1
            return get_company_name(True, i)
        else:
            return res
    else:
        return res


a = get_company_name(unique=True, i=1)
print(a)




