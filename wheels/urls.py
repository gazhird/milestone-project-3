
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('admin/', admin.site.urls),
]
