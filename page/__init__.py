from selenium.webdriver.common.by import By

"""百年奥莱 登录配置数据"""
# 点击 我
login_me = By.ID, "com.yunmall.lc:id/tab_me"
# 点击已有账号去登录
login_username_link = By.XPATH,"//*[contains(@text,'已有账号，去登录')]"
# 输入账号
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 输入密码
login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 点击登录按钮
login_click_login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 获取登录后信息
login_nikename = By.ID, 'com.yunmall.lc:id/tv_user_nikename'
# 点击设置按钮
login_click_setting_btn = By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image'
# 消息推送
login_message_push = By.ID, "com.yunmall.lc:id/setting_notification"
# 修改密码
login_update_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
# 点击退出按钮
login_out_log = By.ID, "com.yunmall.lc:id/setting_logout"
# 确认退出
login_yes_out = By.ID, "com.yunmall.lc:id/ymdialog_right_button"

