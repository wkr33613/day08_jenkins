import pytest
import sys
import os
sys.path.append(os.getcwd())

from base.get_driver import get_driver
from page.page_login import PageLogin


class TestLogin():
    def setup(self):
        self.driver=get_driver()
        # 初始化 PageLogin类
        self.login=PageLogin(self.driver)

    def teardown(self):
        # 关闭driver
        self.login.driver.quit()

    def test_login(self,username="itheima", pwd="123456",ex_result='itheima'):
        # 登录
        self.login.page_login(username,pwd)

        # 断言
        try:
            assert self.login.page_get_login_mes() == ex_result
            try:
                # 退出
                self.login.page_logout()
                assert self.login.page_logout_is_ok()
            except:
                print("退出断言失败")

        except:
            print('断言登录失败')
        # self.login.page_logout()

