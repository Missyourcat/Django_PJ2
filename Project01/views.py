import datetime

from django.contrib import auth
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render

from Project01.forms import BookInfoForm, BookInfoModelForm
from Project01.models import BookInfo, BookType, AccountInfo


# Create your views here.
class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age


def index(request):
    str01 = '模板变量02'
    str02 = 'hello'
    date01 = datetime.datetime.now()
    dict01 = {'tom': 666, 'cat': '999', 'ok': '111'}
    # 创建对象
    zhangsan = Person("张三", 15)
    # 列表
    list01 = ['java', 'python', 'javascript']
    # 元组
    tuple01 = ('python', 1, 3.14, False)
    content_value = {'msg01': str01, 'msg02': dict01, 'msg03': zhangsan, 'msg04': list01, 'msg05': tuple01,
                     'msg06': str02, 'msg07': date01}

    return render(request, 'index.html', context=content_value)


def to_course(request):
    """
    跳转课程页面
    :param request:
    :return:
    """
    return render(request, 'course.html')


def bookList(request):
    """
    图书列表查询
    :param request:
    :return:
    """
    # 查询所有信息
    bookList = BookInfo.objects.all()
    # context_value = {'title': '图书列表', 'bookList': bookList}
    # return render(request, 'book/list.html', context_value)

    # 获取数据集的第一条数据的bookName属性值
    # print(bookList[0].bookName)
    # 返回前2条数据 select * from t_book limit 2
    # bookList = BookInfo.objects.all()[:2]
    # 查询指定字段
    # bookList = BookInfo.objects.values("bookName", "price", 'bookType')
    # 查询指定字段 数据以列表方式返回，列表元素以元组表示
    # bookList = BookInfo.objects.values_list("bookName", "price")
    # 获取单个对象，一般是根据id查询
    # book = BookInfo.objects.get(id=2)
    # 返回满足条件id=2的数据，返回类型是列表
    # bookList = BookInfo.objects.filter(id=2)
    # bookList = BookInfo.objects.filter(price=88, id=2)
    # filter的查询条件可以设置成字典格式
    # d = dict(price=100, id=1)
    # bookList = BookInfo.objects.filter(**d)
    # print(book.bookName)
    # SQL的or查询，需要引入Q，from django.db.models import Q
    # 语法格式：Q(field=value)|Q(field=value) 多个Q之间用"|"隔开
    # bookList = BookInfo.objects.filter(Q(id=1) | Q(price=88))
    # SQL的不等于查询，在Q查询中用“~”即可
    # bookList = BookInfo.objects.filter(~Q(id=1))
    # 使用count()方法，返回满足查询条件后的数据量
    # t = BookInfo.objects.filter(id=2).count()
    # print(t)
    # distinct()方法，返回去重后的数据
    # bookList = BookInfo.objects.values('bookName').distinct()
    # 使用order_by设置排序
    # bookList = BookInfo.objects.order_by("-id")
    # annotate类似于SQL里面的GROUP BY方法
    # 如果不设置values，默认对主键进行GROUIP BY分组
    # r = BookInfo.objects.values('bookType').annotate(Sum('price'))
    # print(r)
    # r2 = BookInfo.objects.values('bookType').annotate(Avg('price'))
    # print(r2)

    # bookList = BookInfo.objects.all()
    # p = Paginator(bookList, 2)
    # bookListPage = p.page(1)
    # print(bookList)
    # print("总记录数：", BookInfo.objects.count())
    # print(bookList[0].bookName)
    # bookList = BookInfo.objects.filter(bookName__contains='思想')
    # bookList = BookInfo.objects.filter(price__gte=5)
    # bookList = BookInfo.objects.filter(price__gte=5)

    # context_value = {'title': '图书列表', 'bookList': bookListPage}

    # bookList = BookInfo.objects.extra(where=['price>%s'], params=[90])

    # bookList = BookInfo.objects.raw("select * from t_book where price>%s", params=[10])

    # cursor: CursorDebugWrapper = connection.cursor()
    # cursor.execute('select count(*) from t_book where price>%s', params=[90])
    # print(cursor.fetchone())
    context_value = {'title': '图书列表', 'bookList': bookList}
    return render(request, 'book/list.html', context_value)


def bookList2(request):
    """
    多表查询，正向查询和反向查询
    :param request:
    :return:
    """
    # 正常查询
    book: BookInfo = BookInfo.objects.filter(id=2).first()
    print(book.bookName, book.bookType.bookTypeName)

    # 反向查询
    bookType: BookType = BookType.objects.filter(id=1).first()
    print(bookType.bookinfo_set.first().bookName)
    print(bookType.bookinfo_set.all())

    context_value = {'title': '图书列表', 'bookList': bookType.bookinfo_set.all()}
    return render(request, 'book/list.html', context_value)


def preAdd(request):
    """
    预处理,添加操作
    :param request:
    :return:
    """
    bookTypeList = BookType.objects.all()
    print(bookTypeList)
    context_value = {'title': '图书添加', 'bookTypeList': bookTypeList}
    return render(request, 'book/add.html', context_value)


def preAdd2(request):
    """
    预处理,添加操作
    :param request:
    :return:
    """
    form = BookInfoForm(request.POST)
    context_value = {'title': '图书添加', 'form': form}
    return render(request, 'book/add2.html', context_value)


def preAdd3(request):
    """
    预处理,添加操作
    :param request:
    :return:
    """
    form = BookInfoModelForm(request.POST)
    context_value = {'title': '图书添加', 'form': form}
    return render(request, 'book/add2.html', context_value)


def preUpdate(request, id):
    """
    预处理，修改操作
    :param request:
    :return:
    """
    print('id:', id)
    book = BookInfo.objects.get(id=id)
    print(book.bookName)
    bookTypeList = BookType.objects.all()
    print(bookTypeList)
    context_value = {'title': '图书添加', 'bookTypeList': bookTypeList, 'book': book}
    return render(request, 'book/edit.html', context_value)


def add(request):
    """
    图书添加
    :param request:
    :return:
    """
    # print(request.POST.get("bookName"))
    # print(request.POST.get("publishDate"))
    # print(request.POST.get("bookType_id"))
    # print(request.POST.get("price"))
    book = BookInfo()
    book.bookName = request.POST.get("bookName")
    book.publishDate = request.POST.get("publishDate")
    # book.bookType_id = request.POST.get("bookType_id")
    book.bookType_id = request.POST.get("bookType")

    book.price = request.POST.get("price")
    book.save()
    # 添加数据后，可以获取id
    print('id:', book.id)
    return bookList(request)


def update(request):
    """
    图书修改
    :param request:
    :return:
    """
    book = BookInfo()
    book.id = request.POST.get("id")
    book.bookName = request.POST.get("bookName")
    book.publishDate = request.POST.get("publishDate")
    book.bookType_id = request.POST.get("bookType_id")
    book.price = request.POST.get("price")
    book.save()

    return bookList(request)


def delete(request, id):
    """
    图书删除
    :param request:
    :return:
    """
    BookInfo.objects.get(id=id).delete()
    # BookInfo.objects.filter(price__gte=90).delete()
    # BookInfo.objects.all().delete()
    return bookList(request)


# def transfer(request):
#     """
#     模拟转账
#     :param request:
#     :return:
#     """
#     a1 = AccountInfo.objects.filter(user='张三')
#     a1.update(account=F('account') + 100)
#     a2 = AccountInfo.objects.filter(user='李四')
#     a2.update(account=F('account') - 100 / 0)
#     return HttpResponse('ok')


@transaction.atomic
def transfer(request):
    """
    模拟转账
    :param request:
    :return:
    """
    # 开启事务
    sid = transaction.savepoint()
    try:
        a1 = AccountInfo.objects.filter(user='张三')
        a1.update(account=F('account') + 100)
        a2 = AccountInfo.objects.filter(user='李四')
        a2.update(account=F('account') - 100)
        # 提交事务
        transaction.savepoint_commit(sid)
    except Exception as e:
        print('异常信息', e)
        transaction.savepoint_rollback(sid)
    return HttpResponse('ok')


def to_register(request):
    """
    跳转注册页面
    :param request:
    :return:
    """
    return render(request, 'auth/register.html')


def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    result = User.objects.filter(username=username)
    if result:
        return render(request, 'auth/register.html',
                      context={'errorInfo': "用户名存在", 'username': username, 'password': password})
    User.objects.create_user(username=username, password=password)
    return render(request, 'auth/login.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 通过auth模块来验证加密后的密码，校验成功返回用户对象，否则返回NOne
    resUser: User = auth.authenticate(username=username, password=password)
    print(resUser, type(resUser))
    if resUser and resUser.is_active:
        # 用户登录成功之后(返回给客户端登录的凭证或者说是令牌，随机字符串)
        auth.login(request, resUser)
        return render(request, 'auth/index.html')
    else:
        return render(request, 'auth/login.html',
                      context={'errorInfo': '用户密码错误', 'username': username, 'password': password})


def to_login(request):
    return render(request, 'auth/login.html')


def setPwd(request):
    """
    修改密码
    :param request:
    :return:
    """
    if request.method == 'POST':
        oldPwd = request.POST.get('oldPwd')
        print(oldPwd)
        newPwd = request.POST.get('newPwd')
        # 1.校验用户原密码
        isRight = request.user.check_password(oldPwd)
        if not isRight:
            return render(request, 'auth/setPwd.html',
                          context={'errorInfo': '原密码错误', 'oldPwd': oldPwd, 'newPwd': newPwd})
        # 2.设置新密码 set_password实现加密
        request.user.set_password(newPwd)
        # 3.保存用户信息
        request.user.save()
        return render(request, 'auth/index.html')
    return render(request, 'auth/setPwd.html')


def logout(request):
    """
    用户注销
    :param request:
    :return:
    """
    auth.logout(request)
    return render(request, 'auth/index.html')


def to_index(request):
    """
    跳转主页
    :param request:
    :return:
    """
    return render(request, 'auth/index.html')
