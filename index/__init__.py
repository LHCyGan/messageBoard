from django.apps import AppConfig
import os

# 修改APP在Admin后台显示的名称
# default_app_config的值来自app.py的类名
default_app_config = 'index.IndexConfig'

# 获取当前APP的命名
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '信息管理'
