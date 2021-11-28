# -*- coding: utf-8 -*-
"""
    @File: test_02_customer_create.py
    @Desc: 
    @Time: 2021/11/16 10:15 下午
    @Author: Wan Wenlong
"""
import pytest
from utils.page_details.pc_agent.page_01_login import login
from utils.page_details.pc_agent.page_02_customer_create import CustomerCreate
from utils.excel import *
from utils.base_page import save_error_screenshot
import time
from utils.base_page import get_driver
from main.run import driver


class TestCreateCustomer:

    sheet = get_sheet('test_02_customer_create.xlsx')
    pre_data = get_pre_info(sheet)
    data = get_data(sheet)

    def setup_class(self):
        if driver:
            self.driver = driver
        else:
            self.driver = get_driver('chrome')

        self.driver.get(self.pre_data[0])
        login(self.driver, self.pre_data[1]['account'], self.pre_data[1]['password'])

    def teardown_class(self):
        self.driver.quit()

    @save_error_screenshot
    @pytest.mark.create_customer
    @pytest.mark.parametrize('user_info', data)
    @pytest.mark.skipif(pre_data[2] not in ('Y', 'y'), reason='标记不执行')
    def test_create_customer(self, user_info):
        f1 = CustomerCreate(driver)
        f1.switch_create_customer()
        f1.input_customer_source(user_info['customer_source'])
        f1.input_customer_name(user_info['customer_name'])
        f1.input_customer_phone_master(user_info['customer_phone_master'])
        f1.select_customer_house_property(user_info['customer_property'])
        f1.click_submit()
        time.sleep(5)
        assert '客户创建成功！' in driver.page_source


if __name__ == '__main__':
    pytest.main(['-s', __file__])


