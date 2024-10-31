# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xy_django_app_feedback",  # 名称为以后pip安装包的名字，后面最好加上用户名，避免名称冲突
    version="0.0.1",
    author="helios",
    author_email="yuyangit.0515@qq.com",
    description="反馈模型",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://8.135.31.13:6402/beachstudio/opensource/xy/service/python/xy-web-service/library/xy_django_app/xy_django_app_feedback.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "xy_django_serializer",
        "xy_django_model",
        "xy_django_app_resource",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
