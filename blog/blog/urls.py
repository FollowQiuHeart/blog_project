"""
项目路由主入口文件；
二级路由在blog应用下的url.py文件中

myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.views.static import serve  # 处理静态文件
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from myblog import views
from django.conf.urls.static import static

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # django-jet 路由
    path('admin/', admin.site.urls),    # 后台管理系统
    path('', views.Index.as_view(), name='index'),   # 首页
    path('blog/', include(('myblog.urls', 'myblog'), namespace='myblog')),  # 定义二级路由
    # url(r'^admin/', admin.site.urls),
    # url(r"test/",views.test),
    # http://127.0.0.1:8000/v1/user
    # url(r"^v1/users", include("user.urls")),
    # http://127.0.0.1:8000/v1/tokens
    # url(r"^v1/tokens", include("wtoken.urls")),
    #   http://127.0.0.1:8000/v1/topic
    # url(r"^v1/topics", include("topic.urls")),
    # http://127.0.0.1:8000/v1/topic
    # url(r"^v1/messages", include("message.urls"))
]

#绑定media_url 和 media_root,显性操作
#127.0.0.1:8000/media/ ->  MEDIA_ROOT
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    #  配置静态文件访问处理
    urlpatterns.append(url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}))
    urlpatterns.append(url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}))

# 全局页面配置
handler403 = 'myblog.views.page_not_look'
handler404 = 'myblog.views.page_not_found'
handler500 = 'myblog.views.page_error'
