# coding=utf-8
__author__ = 'gabriel'

from django.contrib import admin
from utilidades.models import Ciudad, Region, ProxyUnidad, ProxyFamilia

admin.site.register(Ciudad)
admin.site.register(Region)
admin.site.register(ProxyUnidad)
admin.site.register(ProxyFamilia)