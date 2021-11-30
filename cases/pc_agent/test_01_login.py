# -*- coding: utf-8 -*-
"""
    @File: test_01_login.py
    @Desc: 
    @Time: 2021/10/22 上午10:33
    @Author: Wan Wenlong
"""
import pytest
from utils.base_page import save_error_screenshot, BasePage
from utils.page_details.pc_agent.page_01_login import LoginPage
from utils.excel import *


class TestLogin:
    sheet = get_sheet('test_01_login.xlsx')
    data = get_data(sheet)
    pre_data = get_pre_info(sheet)
    driver = BasePage.get_driver()

    # def setup_class(self):
    #     try:
    #         self.driver = driver
    #     except Exception as e:
    #         self.driver = get_driver('chrome')
    #
    # def teardown_class(self):
    #     self.driver.quit()

    @save_error_screenshot
    @pytest.mark.login
    @pytest.mark.parametrize('user_info', data)
    @pytest.mark.skipif(pre_data[2] not in ('Y', 'y'), reason='标记不执行')
    def test_login(self, user_info):
        # self.driver = driver
        f = LoginPage()
        self.driver.get(self.pre_data[0])
        f.input_user(user_info['account'])
        f.input_pwd(user_info['password'])
        f.click_login()
        assert user_info['response'] in self.driver.page_source, '校验失败'


if __name__ == '__main__':
    pytest.main(['-s', __file__])





