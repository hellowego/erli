# coding=utf-8
'''
Created on 2014-10-8

@author: Administrator
'''
from django.shortcuts import render


def home(request):
    """网站首页."""    
    return render(request, 'index.html')