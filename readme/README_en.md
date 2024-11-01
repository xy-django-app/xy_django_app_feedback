<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_django_app_feedback/readme/README_en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_feedback

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## Description

Common feedback data model.

## Source Code Repositories

- <a href="https://github.com/xy-django-app/xy_django_app_feedback.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-django-app/xy_django_app_feedback.git" target="_blank">Gitee</a>

## Installation

```bash
# bash
pip install xy_django_app_feedback
```

## How to use


##### 1. Direct import

- ###### 1. Setting global configuration

Add the following configuration to the settings.py file in the Django project.  
For example:[settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "xy_django_app_resource",
    "xy_django_app_feedback",
    "Demo",
    "Resource",
    "Media",
]

```

- ###### 2. Run the project

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start

# 启动工程后访问 http://127.0.0.1:8401/admin 验证信息管理系统
```

##### 2. Custom

- ###### 1. Create the Feedback module

> Operation [Sample Project](../samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp Feedback
# Feedback 模块创建在 source/Runner/Admin/Feedback 
```

- ###### 2. Setting global configuration

Add the following configuration to the settings.py file in the Django project.  
For example: [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Demo",
    "Resource",
    "Media",
    "xy_django_app_resource",
    "Feedback",
]

```

- ###### 3. Add the following code to the [models.py](../samples/xy_web_server_demo/source/Runner/Admin/Feedback/models.py) of the  [Feedback](../samples/xy_web_server_demo/source/Runner/Admin/Feedback) module

```python
# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from xy_django_app_feedback.abstracts import MAFeedback


class MFeedback(MAFeedback):
    images = models.ManyToManyField(
        "xy_django_app_resource.MImage",
        verbose_name=_("图片"),
        related_name="%(app_label)s_%(class)s_images",
        blank=True,
    )

    class Meta:
        verbose_name = _("反馈")
        verbose_name_plural = _("反馈")
        app_label = "Feedback"

```

- ###### 4. Add the following code to the [admin.py](../samples/xy_web_server_demo/source/Runner/Admin/Feedback/admin.py) of the [Feedback](../samples/xy_web_server_demo/source/Runner/Admin/Feedback) module

```python
# admin.py
from django.contrib import admin
from .models import *


@admin.register(MFeedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("username", "text")
    filter_horizontal = ["images"]

```

- ###### 5. Run the project

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start

# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户管理系统
```


##### Run [Sample Project](../samples/xy_web_server_demo)

> For detailed usage of the sample project, please go to the following repository <b style="color: blue">xy_web_server.git</b> 
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee</a>

## License
xy_django_app_feedback is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```