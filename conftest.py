# -*- coding: utf-8 -*-
"""
    @File: conftest.py
    @Desc: 
    @Time: 2021/11/1 下午5:58
    @Author: Wan Wenlong
"""
import pytest
from common.base_page import get_driver


@pytest.fixture(name='fx', scope='module', autouse=False)
def open_and_close_browser(browser):
    driver = get_driver(browser)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

