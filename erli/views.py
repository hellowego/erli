# coding=utf-8
'''
Created on 2014-10-8

@author: Administrator
'''
from django.shortcuts import render, render_to_response


def home(request):
    """网站首页."""    
    return render(request, 'index.html')

def checkout(request):
    """快捷支付"""
    return render(request, 'checkout.html')