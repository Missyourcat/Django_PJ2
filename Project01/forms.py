from django import forms
from django.forms import Form, ModelForm

from Project01.models import BookType, BookInfo


# 定义学生form表单
# class StudentForm(ModelForm):
#     class Meta:
#         model = Studentinfo
#         fields = '__all__'
#
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'inputClass', 'id': 'name'}),
#             'age': forms.NumberInput(attrs={'id': 'age'}),
#         }
#         labels = {
#             'name': '姓名',
#             'age': '年龄'
#         }
class BookInfoModelForm(ModelForm):
    class Meta:
        model = BookInfo
        fields = '__all__'
        widgets = {
            'bookName': forms.TextInput(attrs={'class': 'inputClass', 'id': 'bookName', 'placeholder': '请输入书名'}),

        }
        labels = {
            'bookName': '书名',
            'price': '价格',
            'publishDate': '日期',
            'bookType': '类型'
        }


class BookInfoForm(Form):
    """
    图书表单
    """

    bookName = forms.CharField(max_length=20, label='图书名称', required=False,
                               widget=forms.TextInput(attrs={'placeholder': '请输入用户名', 'class': 'inputClass'}))
    price = forms.FloatField(label='图书价格', required=False)
    publishDate = forms.DateField(label='出版日期', required=False)
    # 获取图书类别列表
    bookTypeList = BookType.objects.values()
    # 图书类别以下拉框形式显示，下拉框选项id是图书类别id，下拉框选项文本是图书类别名称
    choices = [(v['id'], v['bookTypeName']) for v, v in enumerate(bookTypeList)]
    bookType_id = forms.ChoiceField(choices=choices, label='图书类别', required=False)
