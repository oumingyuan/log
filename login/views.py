from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse


def home(request):
    return render(request, "login/index.html")


'''用户注册的方法'''


def register(request):
    state = None
    if request.method == 'POST':

        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        # email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        if User.objects.filter(username=username):
            state = 'user_exist'

            return HttpResponse(state)
        else:
            # new_user = User.objects.create_user(username=username, password=password, email=email)
            new_user = User.objects.create_user(username=username, password=password, )
            # new_user.save()

            print("****************************")
            print(new_user)

            return HttpResponse(new_user)


def log_in(request):
    password = request.POST.get('password', '')
    username = request.POST.get('username', '')

    # print(request.headers)
    # print(request.headers["Origin"])

    # origin = request.headers["Origin"]
    # str_list = re.split('://|:', origin)
    # print(str_list)

    if User.objects.filter(username=username):
        user = authenticate(username=username, password=password)
        if user:
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("密码错误")
    else:
        return HttpResponse("用户不存在")


def get_request_info(request):
    # origin = request.headers["Origin"]
    # str_list = re.split('://|:', origin)
    # print(str_list)
    # return HttpResponse(str_list[1])
    return HttpResponse('localhost')


'''

TRUE 是检测合格
false 是检测失败
'''


def check_name(request):
    if request.method == 'POST':

        username = request.POST.get('username', '')
        if User.objects.filter(username=username):

            return HttpResponse(True)
        else:

            return HttpResponse(False)
