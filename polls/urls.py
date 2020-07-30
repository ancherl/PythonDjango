from django.urls import path
from . import views

# 在新版本的Django中， 注意django.urls.path 和 django.urls.re_path的区别
# django.urls.path route参数为一个字符串而不是正则表达式 参数传递需使用路径转换器
# django.urls.re_path route参数是一个正则表达式
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<int:month>/', views.index_with_parameter, name='index_with_parameter'),
    path('login/', views.login_page),
    path('validate/', views.validate),
]