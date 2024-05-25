# import os
# from appium.options.android import UiAutomator2Options
# #from utils import file
#
#
# class Config:
#
#     def __init__(self):
#         self.url = os.getenv('URL')
#
#
#         self.app_wait_activity = os.getenv('APP_WAIT_ACTIVITY')
#         self.local_app = os.getenv('LOCAL_APP')
#         self.timeout = float(os.getenv('TIMEOUT', '10'))
#
#     def to_driver_options(self):
#         options = UiAutomator2Options()
#         options.set_capability("deviceName", self.device_name)
#         options.set_capability("platformVersion", self.platform_version)
#         options.set_capability("app", file.path_apk(self.local_app))
#         options.set_capability("appWaitActivity", self.app_wait_activity)
#         return options
#
#
# config_app = Config()
