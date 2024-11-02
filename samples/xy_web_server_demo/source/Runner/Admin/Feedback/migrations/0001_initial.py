# Generated by Django 5.1.2 on 2024-11-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MFeedback",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "username",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="用户名"
                    ),
                ),
                (
                    "text",
                    models.TextField(blank=True, null=True, verbose_name="反馈内容"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=300, null=True, verbose_name="邮箱"
                    ),
                ),
                (
                    "mobile",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="手机号"
                    ),
                ),
                (
                    "wechat",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="微信"
                    ),
                ),
                (
                    "qq",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="QQ"
                    ),
                ),
                (
                    "weibo",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="微博"
                    ),
                ),
                (
                    "dingding",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="钉钉"
                    ),
                ),
                (
                    "twitter",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="X(Twitter)"
                    ),
                ),
                (
                    "google",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="Google"
                    ),
                ),
                (
                    "facebook",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="Facebook"
                    ),
                ),
                (
                    "instagram",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="Instagram"
                    ),
                ),
                (
                    "tiktok",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="TikTok"
                    ),
                ),
                (
                    "bilibili",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="Bilibili(哔哩哔哩)",
                    ),
                ),
                (
                    "douyin",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="抖音"
                    ),
                ),
                (
                    "update_time",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="更新时间"
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="创造时间"
                    ),
                ),
            ],
            options={
                "verbose_name": "反馈",
                "verbose_name_plural": "反馈",
            },
        ),
    ]