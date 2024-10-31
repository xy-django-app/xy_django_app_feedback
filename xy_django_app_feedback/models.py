from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.


class FeedbackAbstract(models.Model):

    id = models.BigAutoField(primary_key=True)

    username = models.CharField(
        verbose_name=_("用户名"),
        max_length=300,
        null=True,
        blank=True,
    )
    text = models.TextField(
        verbose_name=_("反馈内容"),
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name=_("邮箱"),
        max_length=300,
        null=True,
        blank=True,
    )
    mobile = models.CharField(
        verbose_name=_("手机号"),
        max_length=300,
        null=True,
        blank=True,
    )
    wechat = models.CharField(
        verbose_name=_("微信"),
        max_length=300,
        null=True,
        blank=True,
    )
    qq = models.CharField(
        verbose_name=_("QQ"),
        max_length=300,
        null=True,
        blank=True,
    )
    weibo = models.CharField(
        verbose_name=_("微博"),
        max_length=300,
        null=True,
        blank=True,
    )
    dingding = models.CharField(
        verbose_name=_("钉钉"),
        max_length=300,
        null=True,
        blank=True,
    )
    twitter = models.CharField(
        verbose_name=_("X(Twitter)"),
        max_length=300,
        null=True,
        blank=True,
    )
    google = models.CharField(
        verbose_name=_("Google"),
        max_length=300,
        null=True,
        blank=True,
    )
    facebook = models.CharField(
        verbose_name=_("Facebook"),
        max_length=300,
        null=True,
        blank=True,
    )
    instagram = models.CharField(
        verbose_name=_("Instagram"),
        max_length=300,
        null=True,
        blank=True,
    )
    tiktok = models.CharField(
        verbose_name=_("TikTok"),
        max_length=300,
        null=True,
        blank=True,
    )
    bilibili = models.CharField(
        verbose_name=_("Bilibili(哔哩哔哩)"),
        max_length=300,
        null=True,
        blank=True,
    )
    douyin = models.CharField(
        verbose_name=_("抖音"),
        max_length=300,
        null=True,
        blank=True,
    )
    update_time = models.DateTimeField(
        verbose_name=_("更新时间"),
        auto_now_add=True,
        blank=True,
        null=True,
    )
    create_time = models.DateTimeField(
        verbose_name=_("创造时间"),
        auto_now_add=True,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("反馈")
        verbose_name_plural = _("反馈")
        app_label = "xy_django_app_feedback"

    def __str__(self):
        return f"{self.id}. {self.username} ({self.text})"


class Feedback(FeedbackAbstract):
    images = models.ManyToManyField(
        "xy_django_app_resource.Image",
        verbose_name=_("图片"),
        related_name="%(app_label)s_%(class)s_images",
        blank=True,
    )
