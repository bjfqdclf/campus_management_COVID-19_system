from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth


def my_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=pwd)
        if user:
            auth.login(request, user)
            request.session.set_expiry(129600)  # 3天
            next_url = request.GET.get('next_path', '/test/')
            return redirect(next_url)
        else:
            print('login false...')

    return render(request, 'login.html')


def create_user(request):
    # user = user_operation.creat_user()

    return HttpResponse('ok')


def test(request):
    return HttpResponse('ok')


def test2(request):
    return HttpResponse('test2')
