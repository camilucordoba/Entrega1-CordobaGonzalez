from django.contrib import admin
from django.urls import path, include

from django_base.views import saludo, index, fecha_actual, probando_template, contact, login_view, logout_view, register_view




urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('saludo/<nombre>/', saludo, name = 'saludo'),
    path('fecha_actual/', fecha_actual, name = 'fecha_actual'),
    path('probando-template/', probando_template, name = 'probando_template'),
    path('contact/', contact, name = 'contacto'),
    path('clothes/', include('clothes.urls')),


    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
]