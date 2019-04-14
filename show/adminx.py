from xadmin import views
import xadmin

from show.models import User, Record
from django.utils import timezone
import datetime


class BaseSetting:
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings:
    """
    后台修改
    """
    site_title = '修改后的名称'
    site_footer = '修改后的底部'
    menu_style = 'accordion'  # 开启分组折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)


class UserAdmin(object):
    menu_style = 'accordion'  # 开启分组折叠
    # pass
    list_display = ('name', 'code', 'password', 'log', 'status')  # list
    list_per_page = 50

    ordering = ('id',)

    readonly_fields = ('name', 'email', 'code', 'password', 'status', 'name_pinyin',)


xadmin.site.register(User, UserAdmin)


class RecordAdmin(object):
    menu_style = 'accordion'  # 开启分组折叠
    list_display = ('add_date', 'reporter', 'status')  # list
    readonly_fields = ('add_date', 'reporter', 'status')  # list

    list_per_page = 18


xadmin.site.register(Record, RecordAdmin)
