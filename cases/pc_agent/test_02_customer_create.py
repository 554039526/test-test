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
from utils.util import read_csv, csv_to_dict
from utils.base_page import save_error_screenshot
import time


class TestCreateCustomer:
    # data = read_csv('test_02_customer_create.csv')

    @save_error_screenshot
    @pytest.mark.login
    # @pytest.mark.parametrize('user_info', data[7:])
    def test_create_customer(self, driver):
        self.driver = driver
        self.driver.get('https://relsagent.joyi.cn/agent/home/ag/login/page')
        login(self.driver, '18703651001', 'Beijing@123')
        f1 = CustomerCreate(driver)
        f1.switch_create_customer()
        f1.input_customer_source('source')
        f1.input_customer_name('张三')
        f1.input_customer_phone_master('13300001237')
        f1.select_customer_house_need()
        f1.click_submit()
        time.sleep(5)
        assert '客户创建成功！' in driver.page_source
        driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', __file__])


