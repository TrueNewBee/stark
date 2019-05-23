django路由分发的本质：include
方式一：
    from django.conf.urls import url,include

    urlpatterns = [
        url(r'^web/', include("app01.urls")),
    ]

方式二：
    include函数主要返回有三个元素的元组。
    from django.conf.urls import url,include
    from app01 import urls
    urlpatterns = [
        url(r'^web/', (urls, app_name, namespace)), # 第一个参数是urls文件对象，通过此对象可以获取urls.patterns获取分发的路由。
    ]


    在源码内部，读取路由时：
        如有第一个参数有：urls.patterns 属性，那么子路由就从该属性中后去。
        如果第一个参数无：urls.patterns 属性，那么子路由就是第一个参数。

方式三：
    urlpatterns = [
        url(r'^web/', ([
            url(r'^index/', views.index),
            url(r'^home/', views.home),
        ], app_name, namespace)), # 第一个参数是urls文件对象，通过此对象可以获取urls.patterns获取分发的路由。
    ]