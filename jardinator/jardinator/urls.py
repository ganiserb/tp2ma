from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',
        'publicidades.views.vista_publicidades',
        name='home'),

    url(r'^contacto/$',
        'solicitudes.views.solicitar',
        name='solicitar'),

    url(r'^registro/$',
        'usuarios.views.registro',
        name='registro'),

    url(r'^login/$',
        'django.contrib.auth.views.login',
        name='login'),

    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),

)

admin.site.site_header = 'Jardinator'
