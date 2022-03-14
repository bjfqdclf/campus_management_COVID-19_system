"""web_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app01.view import public_views, admin_views

urlpatterns = [
    # 系统public页面
    path('', public_views.all_login),
    path('login/', public_views.all_login),
    path('logout/', public_views.logout),
    path('not_find/', public_views.url_404),

    path('test/', public_views.test),
    path('test2/', public_views.test2),

    # 管理员页面
    path('admin/home/', admin_views.home),


]
