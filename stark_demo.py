from stark.service.stark import site, ModelStark
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import redirect
from .models import *
"""
可以配置字段:
        1. list_display[]   可以添加自定义展示字段,也可以添加函数名
        2. 父类提供的添加该表额外url的接口 def extra_url  重写这个方法即可
"""


class UserConfig(ModelStark):
    # 自定义展示字段 list_display[]
    list_display = ["name", "email", "depart"]


class ClassConfig(ModelStark):
    # 自定义一个展示函数,然后添加到list_display中
    def display_classname(self, obj=None, header=False):
        if header:
            return "班级名称"
        class_name = "%s(%s)" % (obj.course.name, str(obj.semester))
        return class_name
    list_display = [display_classname, "tutor", "teachers"]


class CusotmerConfig(ModelStark):

    def display_gender(self, obj=None, header=False):
        if header:
            return "性别"
        return obj.get_gender_display()

    def display_course(self, obj=None, header=False):
        if header:
            return "咨询课程"
        temp = []
        for course in obj.course.all():
            s = "<a href='/stark/crm/customer/cancel_course/%s/%s' style='border:1px solid #369;padding:3px 6px'><span>%s</span></a>&nbsp;" % (
            obj.pk, course.pk, course.name,)
            temp.append(s)
        return mark_safe("".join(temp))
    list_display = ["name", display_gender, display_course, "consultant", ]

    def cancel_course(self, request, customer_id, course_id):
        print(customer_id, course_id)
        obj = Customer.objects.filter(pk=customer_id).first()
        obj.course.remove(course_id)
        return redirect(self.get_list_url())

    # 父类给出的添加额外url的接口
    def extra_url(self):
        temp = []
        temp.append(url(r"cancel_course/(\d+)/(\d+)", self.cancel_course))
        return temp

# 有配置类的models注册
site.register(UserInfo, UserConfig)
site.register(ClassList, ClassConfig)
site.register(Customer, CusotmerConfig)

# 没有配置类的models直接注册
site.register(Course)
