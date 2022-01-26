from django.contrib import admin
from .models import *
# Register your models here.

# 修改title 和header
admin.site.site_title = "信息反馈后台平台"
admin.site.site_header = "信息反馈平台"

@admin.register(Message)  #  在Admin后台中注册Message
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'addtime']  #  显示的字段
    search_fields = ['name']  # 允许搜索的字段
    list_filter = ['name']  # 用于筛选的字段
    ordering = ['id']  # 排序  + ’-‘为降序
    date_hierarchy = 'addtime'  # 设置日期选择器
