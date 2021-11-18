# -*- coding: utf-8 -*-
"""
    @File: conftest.py
    @Desc: 
    @Time: 2021/11/1 下午5:58
    @Author: Wan Wenlong
"""
import pytest
from utils.base_page import get_driver

browser = 'chrome'


@pytest.fixture(name='driver', params=['1'], scope='module', autouse=False)
def open_and_close_browser():
    driver = get_driver(browser)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

