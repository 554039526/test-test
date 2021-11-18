# -*- coding: utf-8 -*-
"""
    @File: test_02_customer_create.py
    @Desc: 
    @Time: 2021/11/16 10:15 下午
    @Author: Wan Wenlong
"""
import pytest
from common.page_details.pc_agent.page_01_login import LoginPage
from common.page_details.pc_agent.page_02_customer_create import CustomerCreate


class TestCreateCustomer:

    @pytest.mark.parametrize()
    def test_create_customer(self, driver):
        self.driver = driver
        f = LoginPage(driver)
        f.input_user('18703651001')
        f.input_pwd('Beijing@123')
        f.click_login()
        f1 = CustomerCreate(driver)
        f1.switch_create_customer()
        f1.input_customer_source('source')






