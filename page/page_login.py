# 编写：
# 1.
# 类名：将模块名称以大驼峰写法抄进来，如果有下划线去掉下划线
# 2.
# 函数：
# 每一步操作单独封装一个函数，如果需要组装，最后进行调用单步函数进行组装业务调用方法
import page
from base.base import Base



class PageLogin(Base):
    # 点击我的
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击已有账户，去登录
    def page_click_username_link(self):
        self.base_click(page.login_username_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_login(self):
        self.base_click(page.login_click_login_btn)

    # 获取登录信息，用于断言
    def page_get_login_mes(self):
        return self.base_get_text(page.login_nikename)

    # 点击设置
    def page_click_setting(self):
        self.base_click(page.login_click_setting_btn)

    # 从消息推送拖拽到修改密码
    def page_drag_and_drop(self):
        # 获取消息推送元素
        ele1 = self.base_find_element(page.login_message_push)
        # 获取修改密码元素
        ele2 = self.base_find_element(page.login_update_pwd)
        # 拖拽
        self.base_drag_and_drop(ele1, ele2)

    # 点击退出
    def page_click_out_log(self):
        self.base_click(page.login_out_log)

    # 点击确认
    def page_click_out_log_ok(self):
        self.base_click(page.login_yes_out)

    # 组装业务方法
    # 登录
    def page_login(self, username, pwd):
        # 点我
        self.page_click_me()
        # 点击已有账户，去登录
        self.page_click_username_link()
        # 输入用户名
        self.page_input_username(username)
        # 输入密码
        self.page_input_pwd(pwd)
        # 点击登录
        self.page_click_login()

    # 退出
    def page_logout(self):
        # 点击设置
        self.page_click_setting()
        # 拖拽
        self.page_drag_and_drop()
        # 点击退出
        self.page_click_out_log()
        # 确认退出
        self.page_click_out_log_ok()

    # 断言判断是否退出成功
    def page_logout_is_ok(self):
        try:
            self.base_find_element(page.login_me,timeout=3)
            return  True
        except:
            return False
