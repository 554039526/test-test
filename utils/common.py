# -*- coding: utf-8 -*-
"""
    @File: common.py
    @Desc: 常用业务工具
    @Time: 2021/11/18 10:56 下午
    @Author: Wan Wenlong
"""
import random
from utils.database import select_respIsList
from utils.util import getOptionValue
from faker import Faker


fake = Faker('zh_CN')


def get_phone(business: str, unique=True):
    """
    生成对应业务的手机号
    :param business: 业务， 只能传 company、agent、customer
    :param unique: 是否唯一
    :return:
    """

    phone_tel = fake.phone_number()  # 生成随机手机号

    if unique:  # 是否唯一
        query = ''
        if business == 'agent':
            query = getOptionValue('sql', 'select_agent_mobile').replace('{condition}', "'"+phone_tel+"'")
        elif business == 'company':
            query = getOptionValue('sql', 'select_admin_mobile').replace('{condition}', "'"+phone_tel+"'")
        elif business == 'customer':
            query = getOptionValue('sql', 'select_customer_mobile').replace('{condition}', "'"+phone_tel+"'")
        all_phone = select_respIsList(query)   # 取数据库中已有的手机号，type：list

        if phone_tel in all_phone:  # 判断数据库已存在该手机号则重新生成
            return get_phone(business, unique=True)
        return phone_tel
    return phone_tel


def get_person_name():
    """
    返回人的姓名
    :return:
    """
    return fake.name()


def get_company_name(unique=False):
    """
    返回公司的名称
    :return:
    """
    res = fake.company()  # 随机生成公司名

    if unique:  # 是否唯一
        query = getOptionValue('sql', 'select_office_name').replace('{condition}', "'"+res+"'")
        all_name = select_respIsList(query)
        if res in all_name:
            return get_company_name(True)
        return res
    return res


def get_sms_code(mobile: str, rand=False):
    """
    获取手机号对应的验证码,
    rand = False, 随机获取一个6位数字，用于错误的验证码
    :param mobile:
    :param rand:
    :return:
    """
    if rand:
        res = random.randint(100000, 999999)
    else:
        query = getOptionValue('sql', 'select_sms_by_mobile').replace('{condition}', "'"+mobile+"'")
        sms_code = select_respIsList(query)
        res = sms_code[0]
    return res


def get_id(unique=True):
    """
    获取随机的身份证号码
    :param unique:
    :return:
    """
    pid = fake.ssn()
    if unique:
        query = getOptionValue('sql', 'select_id').replace('{condition}', "'"+pid+"'")
        all_ids = select_respIsList(query)
        if pid in all_ids:
            return get_id(True)
        return pid
    return pid


if __name__ == '__main__':
    print(get_phone(business='customer', unique=True))
