from django.contrib import admin

from Project01.models import BookType, BookInfo

# Register your models here.
# 方法一，将模型直接注册到admin后台
admin.site.register(BookType)


# 自定义类，继承ModelAdmin
@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    # 设置显示字段
    list_display = ['id', 'bookName', 'price', 'publishDate', 'bookType']

    # search_fields = ['bookName', 'publishDate']

    # 重写方法，设置只读字段
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['bookName']
        return self.readonly_fields


# 设置网站标题和应用标题
admin.site.site_title = 'www后台管理'
admin.site.index_title = "图书模块管理"
admin.site.site_header = 'pycharm'
