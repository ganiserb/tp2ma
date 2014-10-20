from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

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

    url(r'^sueldos/$',
        'gestion.views.listar_pago_empleados',
        name='sueldos'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Jardinator'
