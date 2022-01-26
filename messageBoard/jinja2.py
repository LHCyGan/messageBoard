# -*- encoding:utf-8 -*-
# author: liuheng
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment

# 将jinja2模板定义到django环境中
def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse
    })
    return env
