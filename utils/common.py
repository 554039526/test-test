# -*- coding: utf-8 -*-
"""
    @File: common.py
    @Desc: 常用业务工具
    @Time: 2021/11/18 10:56 下午
    @Author: Wan Wenlong
"""
from mimesis import Person, Business
from mimesis.enums import Gender
from mimesis.schema import Schema
import random
from utils.database import select_respIsList
from utils.util import getOptionValue
from faker import Faker


phone = ['13900000000', '13900000001']
p = Person('zh')
b = Business('zh')
fake = Faker('zh_CN')


def get_phone(business: str, unique=True):
    """
    生成对应业务的手机号
    :param business: 业务， 只能传 company、agent
    :param unique: 是否唯一
    :return:
    """

    phone_tel = p.telephone(mask='13#########')  # 生成随机手机号

    if unique:  # 是否唯一
        if business == 'agent':
            query = getOptionValue('sql', 'select_agent_mobile')
        elif business == 'company':
            query = getOptionValue('sql', 'select_admin_mobile')
        all_phone = select_respIsList(query)   # 取数据库中已有的手机号，type：list

        if phone_tel in all_phone:  # 判断数据库已存在该手机号则重新生成
            return get_phone(business, unique=True)
        else:
            return phone_tel
    else:
        return phone_tel


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


def get_company_name(unique=False):
    """
    返回公司的名称
    :return:
    """
    res = b.company() + b.company_type()  # 随机生成公司名

    if unique:  # 是否唯一
        query = getOptionValue('sql', 'select_office_name')
        all_name = select_respIsList(query)
        if res in all_name:
            return get_company_name(True)
        else:
            return res
    else:
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
        query = getOptionValue('sql', 'select_sms_by_mobile').replace('ins', mobile)
        sms_code = select_respIsList(query)
        res = sms_code[0]
    return res


def get_id(unique=True):
    """
    获取随机的身份证号码
    :param unique:
    :return:
    """
    id = fake.ssn()
    if unique:
        query = getOptionValue('sql', 'select_id')
        all_ids = select_respIsList(query)
        if id in all_ids:
            return get_id(True)
        else:
            return id
    else:
        return id
