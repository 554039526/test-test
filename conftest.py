# -*- coding: utf-8 -*-
"""
    @File: conftest.py
    @Desc: 
    @Time: 2021/11/1 下午5:58
    @Author: Wan Wenlong
"""
import pytest
from utils.base_page import BasePage
from utils.page_details.pc_agent.page_01_login import login


@pytest.fixture(name='agent_login', params=['1'], scope='module', autouse=False)
def agent_login(request):
    if '退出登录' not in BasePage.driver.page_source:
        BasePage.driver.get(request.param[0])
        login(request.param[1]['account'], request.param[1]['password'])

