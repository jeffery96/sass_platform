from django.shortcuts import render
from app01 import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegisterModelForm(forms.ModelForm):
    # 重写字段
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误')])
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='密码', widget=forms.PasswordInput())
    code = forms.CharField(label='验证码', )

    class Meta:
        model = models.UserInfo
        fields = '__all__'


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})
